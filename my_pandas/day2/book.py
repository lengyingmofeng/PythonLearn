# @作者 : 叶枫
# @文件 : book.py 
# @时间 : 2021/11/26 10:34
# @版本 ：1.0
# @功能描述:
import pandas as pd
from matplotlib import pyplot

df = pd.read_csv("books.csv")
# print(df.info())
s = df[pd.notnull(df['original_publication_year'])]
data = s.groupby('original_publication_year').count()['title']
print(data.to_string())
# data = df.dropna(subset=[])