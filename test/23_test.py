import pandas as pd

# 学生成绩表
df_grade = pd.read_excel("../course_datas/c23_excel_vlookup/学生成绩表.xlsx")

# 学生信息表
df_sinfo = pd.read_excel("../course_datas/c23_excel_vlookup/学生信息表.xlsx")[["学号", "姓名", "性别"]]

merge_df = pd.merge(left=df_grade, right=df_sinfo, right_on='学号', left_on='学号')

print(merge_df.head())

columns_list = ['班级', '学号','姓名', '性别', '语文成绩', '数学成绩', '英语成绩']
merge_df = merge_df.reindex(columns = columns_list)
print(merge_df)

merge_df.to_excel('hehe.xlsx',index=False)