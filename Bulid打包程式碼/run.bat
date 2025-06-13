@echo off
:: 設定 pyinstaller 路徑（如果 PATH 有設好可以省略）
set PYI=%LOCALAPPDATA%\Programs\Python\Python311\Scripts\pyinstaller.exe

:: 打包指令
"%PYI%" --noconsole --onefile ^
--add-data "bus_stops_with_lat_lon.csv;." ^
--add-data "run.bat;." ^
--hidden-import=streamlit.runtime.scriptrunner.script_run_context ^
公車動態查詢.py

pause
