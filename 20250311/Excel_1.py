import pandas as pd

# 讀取 Excel 檔案
df = pd.read_excel('0311.xlsx')

# 假設你的欄位名稱是 'x' 和 'y'
df['sum'] = df['x'] + df['y']

# 印出相加結果
print(df['sum'])