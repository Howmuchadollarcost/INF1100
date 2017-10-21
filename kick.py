"""
air resistance on a football
"""
from math import *
g = 9.81 #gravity
def kick(C_D,g_dens,a,V,m):
    A = pi*a**2
    F_d = 0.5*C_D*g_dens*A*V**2
    F_g = m*g
    return F_d,F_g

def km_h2m_s(km_h):
    m_s = (5./18)*km_h
    return m_s

v_soft =kick(0.2,1.2,11./100, km_h2m_s(10),0.43)
v_hard = kick(0.2,1.2,11./100, km_h2m_s(120),0.43)

print("The drag force is %.1f N for the fast ball, and %.3f N for the slow ball. The gravitational force is %.2f N for both balls " %(v_hard[0],v_soft[0],v_hard[1]))
