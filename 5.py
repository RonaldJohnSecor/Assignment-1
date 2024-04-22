import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = (x**2 + x + 10)/(2*x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = (x^2 + x + 10)/(2x)$')
plt.grid(True)
plt.show()