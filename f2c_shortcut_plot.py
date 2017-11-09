import matplotlib.pyplot as plt
import numpy as np

def f2c_approx(f):
    return (f-30)/2.0
def f2c_exact(f):
    return (f - 32)*5.0/9

f_val = np.linspace(-20,120)

def plot_both(f_val):
    x = plt.plot(f_val,f2c_approx(f_val))
    y = plt.plot(f_val,f2c_exact(f_val))
    return x,y

plot_both(f_val)

plt.xlabel('Farenheit(f)')
plt.ylabel('Celsius (c)')
plt.legend(['f2c_approx','f2c_exact'])
plt.show()
