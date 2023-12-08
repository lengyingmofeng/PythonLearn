import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
plt.figure(figsize=(10, 8), dpi=80)
color = np.random.random(3000).reshape((1000, 3))
size = np.random.randint(0, 100, 1000)
plt.scatter(x, y, c=color, s=size, marker="*")
plt.show()