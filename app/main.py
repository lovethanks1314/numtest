from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from .supabase_client import supabase

app = FastAPI(title="Number Tracker API")

# 資料模型
class NumberEntry(BaseModel):
    value: int

# API 路由
@app.post("/api/numbers")
async def create_number(entry: NumberEntry):
    try:
        response = supabase.table("numbers").insert({"value": entry.value}).execute()
        if hasattr(response, 'error') and response.error:
            raise HTTPException(status_code=400, detail=str(response.error))
        return {"status": "success", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/numbers")
async def get_numbers():
    try:
        response = supabase.table("numbers")\
            .select("*")\
            .order("created_at", desc=True)\
            .limit(50)\
            .execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 靜態檔案路由
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("app/static/index.html")

@app.get("/admin")
async def read_admin():
    return FileResponse("app/static/admin.html")

@app.get("/api/config")
async def get_config():
    # 僅暴露 URL 與 ANON_KEY 給前端，絕對不要暴露 SERVICE_ROLE_KEY
    return {
        "supabase_url": os.getenv("SUPABASE_URL"),
        "supabase_anon_key": os.getenv("SUPABASE_ANON_KEY")
    }

# Render 啟動環境變數檢核
@app.on_event("startup")
async def startup_event():
    print(f"App is starting in {os.getenv('APP_ENV', 'development')} mode")
