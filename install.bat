@echo off
chcp 65001
echo [迫真計算器 安裝器] 開始檢查環境...

:: 檢查 Python 是否安裝
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未偵測到 Python，請先安裝 Python 3.6 以上版本。
    echo 下載網址：https://www.python.org/downloads/windows/
    pause
    exit /b
) else (
    echo ✅ 偵測到 Python...
)

:: 創建虛擬環境（可選）
REM python -m venv venv
REM call venv\Scripts\activate

:: 安裝必要套件（若無使用外部第三方庫，可以省略）
echo [步驟] 檢查是否需要安裝 tkinter...
python -c "import tkinter" 2>NUL
if errorlevel 1 (
    echo ❌ tkinter 未安裝，請重新安裝 Python 並勾選 tkinter 選項！
    pause
    exit /b
) else (
    echo ✅ tkinter 已安裝
)

:: 安裝自訂 utils.py 需要的內建模組（如有外部需求，請加入 requirements.txt）
IF EXIST requirements.txt (
    echo [步驟] 安裝 requirements.txt 中套件...
    pip install -r requirements.txt
) else (
    echo 沒有 requirements.txt，略過 pip 安裝...
)

:: 啟動程式
echo [步驟] 啟動迫真計算器...
python app\ui.py
pause
