# WorldModel 2D→3D Pipeline (Lightweight Runnable Stub)

MODEL EXECUTION DISABLED – STRUCTURE ONLY

這個專案已整理為**單一 Jupyter Notebook**，可直接匯入 Kaggle 或在本地執行。內容全部是 stub，不包含模型執行、權重下載、訓練流程、或外部 API 呼叫。執行內容只會處理 dummy data，輸出也都是 placeholder。

## 本地執行方式（超輕量）

1. 開啟 `notebooks/kaggle_stub.ipynb`
2. 保持 `PROFILE = "tiny"`，並把 `RUN_ONCE = True`
3. 執行整份 Notebook（只跑 dummy data）

## Kaggle 執行方式（超輕量）

1. 進入 Kaggle → New Notebook
2. 匯入 `notebooks/kaggle_stub.ipynb`
3. 保持 `PROFILE = "tiny"`，並把 `RUN_ONCE = True`
4. 執行一次（只跑 dummy data）

## 輕量化保護機制

- `PROFILE` 提供 tiny/small/medium 預設
- `validate_config` 會限制上限
- `HARD_LIMIT_CELLS` 是硬上限，`SAFE_MODE` 會阻止執行

## 重要限制

- MODEL EXECUTION DISABLED – STRUCTURE ONLY
- 不假設 GPU
- 不需要 Kaggle 憑證
- 不會下載資料或權重

## 檔案結構

- `notebooks/kaggle_stub.ipynb`: 完整 pipeline stub（單一 Notebook）
- `.github/workflows/kaggle.yml`: 只是示意用的 workflow stub（不會觸發）
- `requirements.txt`: 無額外相依
