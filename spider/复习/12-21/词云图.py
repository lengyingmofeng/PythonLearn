# @作者 : 叶枫
# @文件 : 词云图.py 
# @时间 : 2021/12/21 20:56
# @版本 ：1.0
# @功能描述:
import jieba
import pandas as pd
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from wordcloud import WordCloud
df = open('黑话.txt', encoding='utf-8').read()
text = jieba.lcut(df, cut_all=True)
text = " ".join(text)
shape = np.array(Image.open('1.jpg'))
word = WordCloud(
    font_path='C:\Windows\Fonts\simfang.ttf',
    width=800,
    height=800,
    mask=shape,
    background_color="white"
).generate(text)
plt.imshow(word)
plt.axis('off')
plt.savefig('词汇.jpg')
plt.show()

plt.plot()
