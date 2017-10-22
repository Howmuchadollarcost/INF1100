t = []
y = []

g = 9.81
v_0 = 5
n = 5
stop = 2*v_0/g      #last
dt = stop/n         #uniformally spaced interval
"""
for i in range(0,n+1):
    time = i*dt
    y_out = v_0*time - 0.5*g*time**2
    t.append(time)
    y.append(y_out)
    print("%.2f  %.2f" %(t[i],y[i]))


for t,y in zip(t,y):
    print("%.2f  %.2f" %(t,y))
"""

time= [t.append(i*dt) for i in range(0,n+1)]
y =[v_0*time - 0.5*g*time**2 for time in t]
print("V0   :   t")
print("------------------------------")
for i in range(len(time)):

    print("%.2f : %.2f" %(t[i],y[i]))

print("------------------------------")
