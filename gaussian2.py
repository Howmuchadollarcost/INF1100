import numpy as np

def gauss(x,m=0,s=1):
    f1 = 1.0/(np.sqrt(2*np.pi)*s)
    f2 = np.exp(-0.5*((x-m)/s)**2)
    f = f1*f2
    return f

 s
x_min =-5
x_max = 5


print("    |       x |  f(x)   |")
print("        ---------------------")

for i in range(x_min,x_max):
    print ("    |%8.3g | %8.3g|" %(i,gauss(i)))
"""
x = x_min
while x <= x_max:
    print ("    %8.3g  %8.3g" %(x,gauss(x,1,2)))
    x+=1
"""
