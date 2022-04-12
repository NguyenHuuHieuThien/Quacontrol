import pandas as pd
import datetime as dt

df = pd.read_excel('process_data\KH_GIAO_HANG(V2).xlsx',index_col=0)

data_XeDG_TG = df.copy()
data = data_XeDG_TG[['ma_dvcs','ngay_giao','so_luong']]
grb1 = data.groupby(['ma_dvcs','ngay_giao'])['so_luong'].sum()

grb1 = grb1.reset_index()
# grb1 = pd.DataFrame(grb1)
# label = grb1.index.values
print(grb1)