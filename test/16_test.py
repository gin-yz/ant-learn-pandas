import pandas as pd
import numpy as np

fpath = "../datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

# print(df.head(5))

df['month'] = df['ymd'].str[5:7].astype('int')

gp_data = df.groupby('month', as_index=True).agg({'bWendu': [np.mean, np.max], 'yWendu': [np.mean, np.min]})
print(gp_data.loc[1:1,:])

