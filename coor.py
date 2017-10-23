n = 20
b = 10
a = 0

h = (b-a)/n

coor=[]

for i in range(0,n+1):
    xi = a + i*h
    coor.append(xi)
print("a)")
print (coor)


coor = [a+i*h for i in range(n+1)]
print("b)")
print (coor)
