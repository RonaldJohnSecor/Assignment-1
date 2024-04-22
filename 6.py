import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = np.sin(x)/(3*x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('sin(x)/(3x)')
plt.title('$Plot of sin(x) / (3x)$')
plt.grid(True)
plt.show()