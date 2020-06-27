"""
计算日期时间差
"""

import pandas as pd
import datetime as dt

# 方法一
wbs = {
    "wbs": ["job1", "job2", "job3", "job4"],
    "date_from": ["2019-04-01", "2019-04-07", "2019-05-16", "2019-05-20"],
    "date_to": ["2019-05-01", "2019-05-17", "2019-05-31", "2019-06-11"]
}

fd = pd.DataFrame(wbs)
print(fd)
# 返回一个timedelta对象，若需要转化为int
fd['elpased'] = fd['date_to'].apply(lambda x: pd.to_datetime(x)) - fd['date_from'].apply(lambda x: pd.to_datetime(x))
# 转换为int
fd['elpased'] = fd['elpased'].apply(lambda x: x.days)
print(fd)
print('---------------------------')

# 方法二

wbs2 = {
    "wbs": ["job1", "job2", "job3", "job4"],
    "date_from": ["2019-04-01", "2019-04-07", "2019-05-16", "2019-05-20"],
    "date_to": ["2019-05-01", "2019-05-17", "2019-05-31", "2019-06-11"]
}

fd2 = pd.DataFrame(wbs2)
print(fd2)


def elpased_time(x,to_time,from_time):
    form_to = dt.datetime.strptime(x[to_time],'%Y-%m-%d')
    form_from = dt.datetime.strptime(x[from_time],'%Y-%m-%d')
    return (form_to-form_from).days
fd2['elpased'] = fd2.apply(elpased_time, axis=1, args=('date_to','date_from'))
print(fd2)
