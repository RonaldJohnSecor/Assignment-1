import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = np.cos(x)/(5*x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('cos(x)/(5x)')
plt.title('$Plot of cos(x) / (5x)$')
plt.grid(True)
plt.show()