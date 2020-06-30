import numpy as np
import pandas as pd

stocks_df = pd.read_excel('../datas/stocks/互联网公司股票.xlsx')


# set_index_df = stocks_df.set_index(['公司','日期'])
# company_list = np.array(stocks_df['公司'].unique())
# data_list = np.array(stocks_df['日期'].unique())
# print(set_index_df.groupby('公司').agg({'收盘':np.mean,'开盘':np.max}))

series_data = stocks_df.groupby(['公司','日期'])['开盘'].mean()
print(type(series_data))
print(series_data[(slice(None),'2019-10-01')])
# print(series_data[:])
