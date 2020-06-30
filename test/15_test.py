"""
将excel文件读取并拆分,并合并
"""
import pandas as pd
import os

dir_addr = r'../course_datas/c15_excel_split_merge'

source_addr = rf'{dir_addr}/crazyant_blog_articles_source.xlsx'

split_addr = rf'{dir_addr}/spiltDATA'

def splite_data():
    df = pd.read_excel(source_addr)

    usernames = [f'cjs{i}' for i in range(10)]

    col_num = df.shape[0] // 10
    if df.shape[0] % 10:
        col_num += 1

    if not os.path.exists(split_addr):
        os.mkdir(split_addr)

    write_datas = [(index, username, df.loc[col_num * index:col_num * (index + 1)-1, :]) for index, username in
                   enumerate(usernames)]

    for data in write_datas:
        data[2].to_excel(fr'{split_addr}/{data[1]}_{data[0]}.xlsx',index=False)

def concat_data():
    user_file_paths = [rf'{split_addr}/{name}' for name in sorted(os.listdir(split_addr))]

    file_data_list = [pd.read_excel(path) for path in user_file_paths]

    fd  = pd.concat(file_data_list,axis=0,ignore_index=True)

    fd.to_excel(rf'{dir_addr}/concat_data.xlsx',index=False)


if __name__ == '__main__':
    splite_data()

    concat_data()