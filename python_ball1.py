g= 9.82
def vertical(v0,t):
    y = v0*t - 0.5*g*t**2
    return y

x = vertical(5,0.6)
print (x+"  m")
