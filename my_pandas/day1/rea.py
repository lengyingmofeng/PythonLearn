# @作者 : 叶枫
# @文件 : rea.py 
# @时间 : 2021/11/25 19:13
# @版本 ：1.0
# @功能描述:
import pandas as pd
import numpy as np
df = pd.read_excel('team.xlsx')
print(df)
print(df.loc[:10, "name"])

print(np.nan == np.nan)
print(np.nan != np.nan)