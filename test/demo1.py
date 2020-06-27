import pandas as pd
import numpy as np

data = {'name': ['Joe', 'Mike', 'Jack', 'Rose', 'David', 'Marry', 'Wansi', 'Sidy', 'Jason', 'Even'],
        'age': [25, 32, 18, np.nan, 15, 20, 41, np.nan, 37, 32],
        'gender': [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        'isMarried': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)

print(print(df))

print(df.loc[~(df['gender'] == 0),:])


