import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = (x**3/2*x) - 10*x

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y= x^3/2x-10x$')
plt.grid(True)
plt.show()