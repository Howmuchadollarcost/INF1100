q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
"""
a)
"""

print(q[0][0])
print(q[1])
print(q[2][-1])
print(q[1][0])

"""
b)
"""
for i in q:
    for j in range(len(i)):
        print (j)
        
print (type(i))
print(type(j))
print (type(i[j]))


"""
i is lists and j is intefer. i[j] is str.
"""
