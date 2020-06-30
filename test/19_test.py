# groupby.apply(function())function()函数返回的对象会再次拼接
import pandas as pd

# ratings = pd.read_csv(
#     "../datas/movielens-1m/ratings.dat",
#     sep="::",
#     engine='python',
#     names="UserID::MovieID::Rating::Timestamp".split("::")
# )
# print(ratings.head())
# def ratings_norm(x):
#     max_value = x['Rating'].max()
#     min_value = x['Rating'].min()
#     norm_value = max_value-min_value
#     x['ratings_norm'] = x.apply(lambda x:(x['Rating']-min_value)/norm_value,axis=1)
#     return x
#
# ratings = ratings.groupby('UserID').apply(ratings_norm)
# print(ratings)
def find_top_temp(x):
    return x.sort_values(by='bWendu',ascending=False)[["ymd","bWendu"]][:2]

fpath = "../datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
# 新增一列为月份
df['month'] = df['ymd'].str[:7]

top_temp_data = df.groupby('month').apply(find_top_temp)
print(top_temp_data)