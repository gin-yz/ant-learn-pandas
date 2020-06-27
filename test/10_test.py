"""
计算日期时间差
"""

import pandas as pd
import datetime as dt
# 方法一
wbs = {
    "wbs": ["job1", "job2", "job3", "job4"],
    "date_from": ["2019-04-01", "2019-04-07", "2019-05-16","2019-05-20"],
    "date_to": ["2019-05-01", "2019-05-17", "2019-05-31", "2019-06-11"]
}

fd = pd.DataFrame(wbs)
print(fd)
# 返回一个timedelta对象，若需要转化为int
fd['elpased'] = fd['date_to'].apply(lambda x:pd.to_datetime(x))-fd['date_from'].apply(lambda x:pd.to_datetime(x))
# 转换为int
fd['elpased'] = fd['elpased'].apply(lambda x:x.days)
print(fd)

# 方法二