import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'F': ['F0', 'F1', 'F2', 'F3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                      'A': ['A10', 'A11', 'A12', 'A13'],
                      'D': ['D0', 'D1', 'D4', 'D5'],
                      'F': ['F0', 'F1', 'F2', 'F3']})

print(left)
print(right)

print(pd.merge(left=left, right=right,on='F',suffixes=['_left',"_right"]))
