import pandas as pd

df = pd.read_csv("../datas/beijing_tianqi/beijing_tianqi_2018.csv")
print(df)
df.loc[:,'bWendu'] = df['bWendu'].str[:-1].astype('int')
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃','').astype('int')
print(df)

print(df.sort_values(by=['bWendu','ymd'],ascending=[True,False]))