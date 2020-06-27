import pandas as pd
import numpy as np

df = pd.read_excel("../datas/student_excel/student_excel.xlsx", skiprows=2)

print(df)

df.dropna(axis=1, how='all', inplace=True)
df.dropna(axis=0, how='all', inplace=True)
df.fillna(axis=0, inplace=True, value={'分数': 0})
# df.fillna(axis=0, inplace=True, method='ffill')
df['姓名'].fillna(method='ffill',inplace=True)
print(df)

