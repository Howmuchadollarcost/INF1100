from numpy import sqrt,exp,pi,linspace,zeros,zeros_like
from matplotlib.pyplot import *

def h(x):
    return 1.0/sqrt(2*pi)*exp(-0.5*x**2)

n = 41
 

x = linspace(-4,4,n)
y = h(x)
plot(x,y)
show()
"""
#list form (5.1)
n = 41
dn = 8./(n-1)
x_l = [-4+i *dn for i in range(n)]
y =[h(x) for x in x_l]

plot(x_l,y)
show()

#loop version(5.2)
x = linspace(-4,4,41)
x_l= zeros(n)
y = zeros_like(x)
dn = 8./(n-1)
for i in range(len(x)):
    x_l[i] = -4+i*dn
    y[i] = h(x[i])
plot(x_l,y)
show()
"""
