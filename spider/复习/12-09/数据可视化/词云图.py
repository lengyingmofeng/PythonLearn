# @作者 : 叶枫
# @文件 : 词云图.py 
# @时间 : 2021/12/9 16:37
# @版本 ：1.0
# @功能描述:
from wordcloud import WordCloud
import jieba
from matplotlib import pyplot as plt
from collections import Counter

if __name__ == '__main__':
    with open("评论.txt", "r", encoding='utf-8') as fp:
        data = fp.read()
    # 进行分词
    data = jieba.lcut(data, cut_all=False)
    # 统计评论词汇出现的次数
    data2 = Counter(data).most_common(1000)
    print(data2)
    # data_txt = "".join(data).count("不行")
    # print(data_txt)
    data = " ".join(data)
    # 去掉无用词汇
    txt = open("无用词汇.txt", encoding="utf-8").read()
    # generate -> 生成
    # 生成词云图
    con = WordCloud(
        font_path="C:\Windows\Fonts\simfang.ttf",
        width=800,
        height=600,
        background_color="white",
        stopwords=txt,
    ).generate(data)
    plt.imshow(con)
    plt.axis('off')
    plt.show()
