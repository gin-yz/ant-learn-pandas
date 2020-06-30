import pandas as pd
import numpy as np

df = pd.read_csv(
    filepath_or_buffer="../datas/movielens-1m/ratings.dat",
    sep='::',
    names="UserID::MovieID::Rating::Timestamp".split("::"),
    engine="python"
)
print(df.head())

#
# df['DateTime'] = pd.to_datetime(df['Timestamp'],unit='s')
#
# print(df.head())
#
# init_df = df.groupby(by=[df['DateTime'].dt.month,'Rating'])['UserID'].agg(number=np.size)
# print(init_df.head())
#
# print(init_df.unstack().head())
#
# reset_df = init_df.reset_index()
#
# print(reset_df.pivot('DateTime','Rating','number').head())


rate_df = df.groupby(['UserID', 'Rating'])['MovieID'].agg(number=np.size)

print(rate_df.head())
