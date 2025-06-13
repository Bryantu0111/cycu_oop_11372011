@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo [提示] 請勿直接執行 Python 主程式（公車動態查詢.py）
echo 本系統需透過 Streamlit 執行，正在自動啟動...
echo.

streamlit run "公車動態查詢.py"
pause
