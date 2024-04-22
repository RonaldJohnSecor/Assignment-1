import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = (x+2)*(x+3)*(x-4)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('(x+2)(x+3)(x-4)')
plt.title('$Plot of (x+2)(x+3)(x-4)$')
plt.grid(True)
plt.show()