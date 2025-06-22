import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100, 220, 5)
y = 0.5 * x ** 2+2 * x

plt.plot(x, y)
plt.show()