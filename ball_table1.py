g = 9.81
v_0 = 5
n = 5
stop = 2*v_0/g      #last
dt = stop/n         #uniformally spaced interval

print("For loop:")
print("----------------------")
print("V0   :    t")
for i in range(0,n+1):
    t = i*dt
    y = v_0*t - 0.5*g*t**2
    print("....................")
    print("%.2f : %.2f" %(t,y))
print("|----------------------|")




i=0
print("While Loop:")
print("----------------------")
print("V0   :    t")
while(i < n+1):
    t= i*dt
    y = v_0*t - 0.5*g*t**2
    print("....................")
    i+=1
    print("%.2f : %.2f" %(t,y))
print("|----------------------|")


"""
or
t = 0
eps = 1e-10
while t<t_stop+eps:
    y = v_0*t - 0.5*g*t**2
    print("%.2f : %.2f" %(t,y)
    t+=dt

"""
