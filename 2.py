import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y = x**10 - x**8 + x**2 + 1

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = x^10 - x^8 + x^2 +1$')
plt.grid(True)
plt.show()