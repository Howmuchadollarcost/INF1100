"""
import sys
g = 9.81
def ball_pos(t,v0):
    return v0*t - 0.5*g*t**2
t = float(input("Please Enter time(s): " ))
v0 = float(input("Please Enter initial velocity(m/s): "))


if 0 <= t <= (2*v0)/(g):
    y = ball_pos(t,v0)
    print("The position (y) after %.2f s and %.2f m/s is %.2f m" %(t,v0,y))
else:
    print("Time(t) is should be between 0 and %.3f" %(2*v0/g))
    sys.exit(1)
"""
g  = 9.81
import sys

def ball_pos(t,v0,g=9.81):
    return v0*t - 0.5*g*t**2

try:
    t = float(sys.argv[1])
    v0 = float(sys.argv[2])
except IndexError:
    print ("No argument given in the command line")
    try:
        t = float(input("Please Enter time(s): " ))
        v0 = float(input("Please Enter initial velocity(m/s): "))
    except:
        print("No number given")
        sys.exit(1)
except ValueError:
    print("Please give the values in right float form not %s and %s" %(sys.argv[1],sys.argv[2]))
    sys.exit(1)

if 0 <= t <= (2*v0)/(g):
    y = ball_pos(t,v0)
    print("The position (y) after %.2f s and %.2f m/s is %.2f m" %(t,v0,y))
else:
    print("Time(t) is should be between 0 and %.3f" %(2*v0/g))
    sys.exit(1)
