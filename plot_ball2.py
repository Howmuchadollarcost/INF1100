import sys
import numpy as np
import matplotlib.pyplot as plt
g = 9.81
def f(t,v0):
    return v0*t - 0.5*g*t**2

def plot_f(v0):
    t = np.linspace(0,2*v0/g)
    return plt.plot(t,f(t,v0))

v0 = np.array(sys.argv[1:],dtype=np.float)

for i in range(len(v0)):
    plot_f(v0[i])

plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.legend(['v0 =%.2f m/s' %(i) for i in v0])
plt.show()
