import numpy as np
import matplotlib.pyplot as plot
from math import pi 

x = np.arange(0, 3 * pi, 0.1)
sin_x = np.sin(x) 

plot.plot(x, sin_x)
plot.title('Grafik fungsi sin(x)') 
plot.xlabel('x') 
plot.ylabel('sin(x)')
plot.grid(True, which='both') 
plot.axhline(y=0, color='#000000')
plot.show()