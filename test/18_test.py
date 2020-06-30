import pandas as pd

stocks = pd.read_excel('../datas/stocks/互联网公司股票.xlsx')
print(stocks.head())

dict_company_names = {
    "bidu": "百度",
    "baba": "阿里巴巴",
    "iq": "爱奇艺",
    "jd": "京东"
}


def change_name(x):
    return dict_company_names[x['公司'].lower()]


def change_name2(x):
    return dict_company_names[x]


stocks['公司1'] = stocks.apply(change_name, axis=1)
print(stocks)
stocks['公司2'] = stocks['公司'].str.lower().apply(change_name2)
print(stocks)

stocks = stocks.applymap(lambda x: int(x) if type(x) == float else x)
print(stocks)
