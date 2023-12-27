# @作者 : 叶枫
# @文件 : 直方图.py 
# @时间 : 2021/12/14 8:34
# @版本 ：1.0
# @功能描述:
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.DataFrame({'a': np.random.randn(1000) + 1,
                   'b': np.random.randn(1000),
                   'c': np.random.randn(1000) - 1},
                  columns=['a', 'b', 'c'])
print(df)
# alpha 透明度, bins
# df.plot.hist(alpha=0.5, bins=30, range=(-4, 4), density=True, stacked=True, label="真不错")
df.plot.hist(orientation='horizontal', cumulative=True, log=True)
# plt.hist(df, alpha=0.5)
plt.show()