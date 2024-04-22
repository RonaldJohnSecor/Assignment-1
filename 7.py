import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**3 + 2*x**2 - 10*x + 3

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y= x^3 + 2x^2 - 10x + 3$')
plt.grid(True)
plt.show()