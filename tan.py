import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 2 * np.pi, 1000)


frequency = 1  
amplitude = 1  
tangent_wave = amplitude * np.tan(frequency * t)


plt.plot(t, tangent_wave)
plt.title('Gelombang Tan')
plt.xlabel('Waktu')
plt.ylabel('Amplitudo')
plt.grid(True)
plt.show()
