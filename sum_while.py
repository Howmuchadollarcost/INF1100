"""
s = 0;  k = 1 ; M = 100

while k < M:    #This counts from k < M true all the time. So we must iterate the k by one (k+=1) and then since it starts are 2 we must use  M+1 in the condition
    s+= 1/k
    print (s)


"""


s = 0
k = 1
M = 100
"""
For loop
for i in range(k,M+1):
    s = s + 1/i
print (s)
"""


while k < M+1:
    s = 1/k + s
    k += 1
print(s)
