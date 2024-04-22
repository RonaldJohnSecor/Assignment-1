import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,400)
y = x**2 + x - 100

plt.plot(x,y)
plt.xlabel('x', color= 'b')
plt.ylabel('y', color= 'm')
plt.title('$y = x^2 + x -100$')
plt.grid(True)
plt.show()