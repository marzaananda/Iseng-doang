import numpy as np
import matplotlib.pyplot as plt  
from math import pi

x = np.arange(0, 2 * np.pi, 0.2)    
y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x, y1, color="red")
plt.plot(x, y2, color="blue")
plt.legend(["sin(x)", "cos(x)"])
plt.show()  

