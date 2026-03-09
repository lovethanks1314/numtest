# FastAPI + Supabase Number Tracker

一個簡單的數字追蹤 Web App，包含使用者輸入介面與即時更新的管理後台。

## 功能特點

- **FastAPI 後端**: 提供資料寫入與獲取 API。
- **Supabase 整合**: 使用 Supabase 儲存資料。
- **Realtime 管理頁**: 使用 Supabase Realtime 讓後台即時顯示新數據。
- **危險警報**: 當數字 >= 55 時，自動標示為「危險」。
- **部署就緒**: 已配置好 Render 自動部署。

## 專案結構

- `/app`: 後端程式碼與靜態前端網頁。
- `/sql`: 資料庫初始化腳本。
- `render.yaml`: Render 部署配置。

## 本機執行步驟

1. **建立環境變數**:
   複製 `.env.example` 並重新命名為 `.env`，填入您的 Supabase 資訊。
2. **安裝套件**:
   ```bash
   pip install -r requirements.txt
   ```
3. **啟動專案**:
   ```bash
   uvicorn app.main:app --reload
   ```
4. **存取頁面**:
   - 輸入頁: `http://localhost:8000/`
   - 管理頁: `http://localhost:8000/admin`

## Supabase 設定

1. **建立 Table**: 在 SQL Editor 執行 `sql/init.sql` 的內容。
2. **啟用 Realtime**:
   - 進入 **Database** -> **Replication**。
   - 點擊 **supabase_realtime** 的 `Edit`。
   - 將 `numbers` 資料表切換為開啟狀態。

## Render 部署步驟

1. 將此專案推送到 GitHub。
2. 在 Render 選擇 `New +` -> `Blueprint`。
3. 連結您的倉庫，Render 會自動根據 `render.yaml` 進行設定。
4. 在 Render Environment Dashboard 手動填入以下變數：
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`
   - `SUPABASE_SERVICE_ROLE_KEY`

## 安全性說明

目前的 `/admin` 頁面僅作為演示，未包含登入邏輯。在實際生產環境中，建議加入身份驗證保護此路徑。
