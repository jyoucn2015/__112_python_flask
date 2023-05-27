import requests
import pandas as pd
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
response = requests.request('GET',url)
if response.status_code == 200:
    print("連線成功")
    all_data = response.json()
    print(type(all_data))
else:
    print(f"連線失敗:{response.status_code}")



dataFrame = pd.DataFrame(data=all_data,columns=['sna','tot','sbi','sarea','mday','ar','bemp','act'])
min = int(input("請輸入要查詢的可借數量:"))
mask = dataFrame['sbi'] <= min
mask_dataFrame = dataFrame[mask]
mask_dataFrame.to_csv('可借小於3的站點.csv')
filename = f'可借小於{min}的站點.xlsx'
mask_dataFrame.to_excel(filename)