# @作者 : 叶枫
# @文件 : 拼音排序.py 
# @时间 : 2020/10/10 18:11 
# @版本 ：1.0

from xpinyin import Pinyin                                # 导入pinyin类
list_name = ["欧阳志飞", "杨圣波", "田思凯", "唐曦"]
list_result = []
Pinyin = Pinyin()                                         # 创建pinyin对象
for name in list_name:
    list_result.append([Pinyin.get_pinyin(name), name])
print("排序前：", list_result)
list_result.sort()                                        # 拼音排序
for i in range(len(list_result)):                         # 使用len函数得出list_result列表中用多少个下标
    list_result[i] = list_result[i][1]
print("排序后：", list_result)

print(list_name)