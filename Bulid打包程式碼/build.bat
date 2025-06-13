@echo off
"C:\Users\user\AppData\Roaming\Python\Python312\Scripts\pyinstaller.exe" --noconsole --onefile ^
--add-data "bus_stops_with_lat_lon.csv;." ^
--add-data "run.bat;." ^
--hidden-import=streamlit.runtime.scriptrunner.script_run_context ^
"公車動態查詢.py"

pause
