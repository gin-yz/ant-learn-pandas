import pandas as pd


def wendu_type(df):
    if df['bWendu'] > 30:
        return '高温'
    elif df['yWendu'] < -10:
        return '低温'
    else:
        return '常温'


if __name__ == '__main__':
    fpath = "../datas/beijing_tianqi/beijing_tianqi_2018.csv"
    df = pd.read_csv(fpath)

    df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int')
    df.loc[:, 'yWendu'] = df['yWendu'].str[:-1].astype('int')

    # print(df.head(), df.dtypes)
    # df.loc[:, 'wencha'] = df['bWendu'] - df['yWendu']
    # print(df.head())
    #
    # df.loc[:, 'wendu_type'] = df.apply(func=wendu_type,axis=1)
    # df = df.assign(wendu_type=df['bWendu'])
    #
    # print(df.head())
    a,b,c = '1-2-3'.split('-')
    print('{0}:{1}:{2}'.format(a,b,c))

