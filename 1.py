import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = x**2 - 10

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = x^2 - 10$')
plt.grid(True)
plt.show()