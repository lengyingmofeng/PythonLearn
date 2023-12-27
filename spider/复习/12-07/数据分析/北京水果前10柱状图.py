# @作者 : 叶枫
# @文件 : 北京新发地菜价分析.py
# @时间 : 2021/12/7 16:29
# @版本 ：1.0
# @功能描述:
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=10)
df = pd.read_csv("菜价.csv")
df['pubDate'] = df["pubDate"].apply(lambda x: str(x).split(" ")[0])

# 删除为空的数据
# df.dropna(subset=["prodPcat", "place"], inplace=True)

apple = df[(df["prodCat"] == "水果")].sort_values('pubDate')
apple = apple.drop_duplicates()[:30]
apple.set_index('pubDate', inplace=True)

plt.figure(figsize=(20, 8), dpi=80)
plt.bar(apple['prodName'], apple['avgPrice'])
plt.xticks(fontproperties=font, rotation=90)
plt.grid()
plt.savefig("水果图.jpg")
plt.show()
