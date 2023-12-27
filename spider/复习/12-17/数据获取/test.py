# @作者 : 叶枫
# @文件 : test.py 
# @时间 : 2021/12/18 14:43
# @版本 ：1.0
# @功能描述:
import json

df = open("test.json")
text = df.read()
print(json.loads(text))