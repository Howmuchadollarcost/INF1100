"""
Store data in a nested list rows  and columns
"""


v0 = 5.0
g = 9.81
n=5
stop = 2*v0/g
dt = stop/n
"""
t = []
y = []

ty1 = []

for i in range(0,n+1):
    time = i*dt
    y0 = v0*time - 0.5*g*time**2
    t.append(time)
    y.append(y0)

for t,y in zip(t,y):
    ty1.append([t,y])


for t,y in ty1:
    print ("%.2f  %.2f" %(t,y))


"""
#############################################################################
ty2=[]
print("________________________")
print("|----------------------|")
for i in range(0,n+1):
    time = i*dt
    y0 = v0*time - 0.5*g*time**2
    ty2.append([time,y0])
print("|y     |    t |")
print("|----------------------|")
print("|----------------------|")
for t,y in ty2:
    print ("|%.2f  |  %.2f|" %(t,y))
    print("|......................|")
