from cmath import *

def roots(a,b,c):
    q = b*b - 4*a*c
    q_sr = sqrt(q)
    x1 = (-b + q_sr)/(2*a)
    x2 = (-b - q_sr)/(2*a)
    return x1,x2

def test_roots_float():
    a = 1
    b = -4
    c = 3
    ans = roots(a,b,c)
    return ans

def test_roots_complex():
    a = 1
    b = -2
    c = 5
    ans = roots(a,b,c)
    return ans
print(test_roots_float())
print(test_roots_complex())
"""
ns = roots(1,-4,3)

for i in ns:
    print (i)
"""
