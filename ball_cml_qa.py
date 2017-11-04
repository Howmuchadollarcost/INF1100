"""
def ball_pos(t,v0,g=9.81):
    return v0*t - 0.5*g*t**2
t = float(input("Please Enter time(s): " ))
v0 = float(input("Please Enter initial velocity(m/s): "))
y = ball_pos(t,v0)
print("The position (y) after %.2f s and %.2f m/s is %.2f m" %(t,v0,y))
"""
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

y = ball_pos(t,v0)
print("The position (y) after %.2f s and %.2f m/s is %.2f m" %(t,v0,y))
