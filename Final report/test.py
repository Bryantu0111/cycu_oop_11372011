import requests
import certifi
import ssl

# 自動取得正確憑證路徑
ssl_context = ssl.create_default_context(cafile=certifi.where())

response = requests.get("https://www.google.com", verify=certifi.where())
print(response.status_code)
