import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）

# 1）准备数据
movie_name = ['雷神3：诸神黄昏','正义联盟','东方快车谋杀案','寻梦环游记','全球风暴','降魔传','追捕','七十七天','密战','狂兽','其它']

place_count = [60605,54546,45819,28243,13270,9945,7679,6799,6101,4621,20105]

# 2）创建画布
plt.figure(figsize=(10, 8), dpi=100)

# 3）绘制饼图
plt.pie(place_count, labels=movie_name, autopct="%1.2f%%")

# 显示图例
plt.legend(prop="SimHei")

# 添加标题
plt.title("电影排片占比")

# 为了让显示的饼图保持圆形，需要添加axis保证长宽一样
plt.axis('equal')

# 4）显示图像
plt.show()