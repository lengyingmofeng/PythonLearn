# @作者 : 叶枫
# @文件 : 123.py 
# @时间 : 2021/12/12 16:48
# @版本 ：1.0
# @功能描述:

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
length = 7
num = []
for i in range(len(nums)):
    num.append(nums[i])

for i in range(len(nums)):
    nums[(i + k) % length] = num[i]
print(nums)



print(nums[:])