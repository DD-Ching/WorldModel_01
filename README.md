# WorldModel 2D→3D Pipeline (Lightweight Runnable Stub)

MODEL EXECUTION DISABLED – STRUCTURE ONLY

這個專案已整理為**單一 Jupyter Notebook**，可直接匯入 Kaggle 執行。內容全部是 stub，不包含模型執行、權重下載、訓練流程、或外部 API 呼叫。執行內容只會處理 dummy data，輸出也都是 placeholder。

## Kaggle 執行方式

1. 進入 Kaggle → New Notebook
2. 匯入 `notebooks/kaggle_stub.ipynb`
3. 將 `RUN_ONCE = True` 後執行（只跑一次）

## 輕量化保護

- `width/height/depth_slices` 有上限
- `max_cells` 限制總體大小，避免爆掉

## 重要限制

- MODEL EXECUTION DISABLED – STRUCTURE ONLY
- 不假設 GPU
- 不需要 Kaggle 憑證
- 不會下載資料或權重

## 檔案結構

- `notebooks/kaggle_stub.ipynb`: 完整 pipeline stub（單一 Notebook）
- `.github/workflows/kaggle.yml`: 只是示意用的 workflow stub（不會觸發）
- `requirements.txt`: 無額外相依
