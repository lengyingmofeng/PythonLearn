# @作者 : 叶枫
# @文件 : 词云图.py 
# @时间 : 2021/12/13 20:12
# @版本 ：1.0
# @功能描述:
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
with open("../../12-17/数据可视化/他只是看上去不努力.txt", encoding='utf-8') as fp:
    txt = fp.read()

text = jieba.lcut(txt)
text = " ".join(text)
stopword = open("../../12-17/数据可视化/无用词汇.txt", encoding='utf-8').read()
word = WordCloud(
    font_path="C:\Windows\Fonts\SIMLI.TTF",
    width=500,
    height=500,
    background_color="white",
    stopwords=set(stopword)
).generate(text)
# 把轴线给去掉
plt.axis('off')
# 绘制高级图形需调用的函数
plt.imshow(word)
# 显示图形
plt.savefig('图形.jpg')
plt.show()
