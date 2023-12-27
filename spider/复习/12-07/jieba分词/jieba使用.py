# @作者 : 叶枫
# @文件 : jieba使用.py 
# @时间 : 2021/12/7 9:51
# @版本 ：1.0
# @功能描述:
import jieba
text = "            逍遥叹，东风破，一路生花，德玛西亚               "
# strip()去除两边空格
print("".join(jieba.lcut(text)).strip().replace("，", ""))
print(jieba.lcut(text, cut_all=True))