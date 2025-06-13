
# 台北市公車動態查詢系統

本系統提供台北市公車路線與即時到站查詢功能，使用者可輸入起訖站點，自動查找直達或轉乘建議，並以互動地圖呈現路線與預估資訊。

---

## 📦 內容說明

| 檔案名稱                 | 用途說明 |
|--------------------------|-----------|
| `公車動態查詢.py`         | 主程式（使用 Streamlit 啟動 Web 介面） |
| `bus_stops_with_lat_lon.csv` | 公車站點經緯度資料檔（需與主程式同一資料夾） |
| `requirements.txt`        | 所需 Python 套件清單 |
| `run.bat`                | Windows 使用者一鍵啟動用批次檔 |
| `README.md`              | 使用說明文件（本檔） |

---

## 💻 安裝與使用方式

### 第一步：安裝 Python

請至 [https://www.python.org/](https://www.python.org/) 下載並安裝 Python 3.9 或以上版本。

建議安裝時勾選 `Add Python to PATH`。

---

### 第二步：安裝必要套件

打開命令提示字元（cmd），切換到本資料夾，輸入以下指令安裝依賴：

```bash
pip install -r requirements.txt
playwright install
```

---

### 第三步：執行程式（請擇一方式操作）

#### ✅ 方法一（推薦）：雙擊 `run.bat`

❌ 請勿直接打開 `公車動態查詢.py` 並按執行鍵（這樣無法正確啟動）
✅ 請務必使用 `run.bat` 或輸入指令：`streamlit run 公車動態查詢.py`

- 自動開啟查詢系統介面，無須額外輸入指令
- 若出現 Windows 安全性提示，請點選「**更多資訊 → 仍要執行**」
- 此 `run.bat` 檔已設為 `UTF-8 with BOM` 編碼，能正確執行中文檔名

#### 🧑‍💻 方法二：手動輸入指令啟動

若偏好使用命令列操作，請在本資料夾下輸入：

```bash
streamlit run 公車動態查詢.py
```

啟動成功後會於瀏覽器開啟 `http://localhost:8501`

---

## 📁 資料夾範例結構

請務必將所有檔案放在同一層資料夾內：

```
taipei_bus_query/
├── 公車動態查詢.py
├── bus_stops_with_lat_lon.csv
├── requirements.txt
├── README.md
└── run.bat
```

---

## ⚠️ 注意事項

- 📶 本系統需連網以查詢臺北市 eBus 即時資訊
- 📍 起訖站請使用下拉選單選取，避免手動輸入錯誤
- 🌐 若瀏覽器未自動開啟，可手動輸入網址：http://localhost:8501
- 🛡️ `run.bat` 如出現「SmartScreen 安全警告」，請點「更多資訊 → 仍要執行」

---

## 📌 聯絡與製作資訊

製作團隊：CYCU_OOP_第三組  
學系單位：中原大學 土木工程學系  
