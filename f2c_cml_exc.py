import sys
"""
print("Farenheit to Celsius Converter")
f = float(input("Enter Farenheit: "))
"""
def c(f):
    return (f - 32)* 5.0/9

def read_F():
    try:
        f = float(sys.argv[1])
    except IndexError:
        print ("No argument in the command line")
        try:
            f = float(input("Enter F: "))
        except:
            print ("not a number!!")
            sys.exit(1)
    except ValueError:
        print("The Farenheit Value has to be a float, not %s" %(sys.argv[1]))
        sys.exit(1)
    return float(f)
f_deg = read_F()
c_deg = c(f_deg)

print ("%.2f F is %.2f C" %(f_deg,c_deg))
