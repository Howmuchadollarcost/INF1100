import numpy as np
import matplotlib.pyplot as plt
def f(x,t):
    return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))
n = 400
x = np.linspace(-4,4,n)
t = 0
plt.plot(x,f(x,t))
plt.xlabel('x')
plt.ylabel('Amp')
plt.savefig('wave_packet.png')
plt.show()
