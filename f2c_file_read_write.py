"""
print("Farenheit to Celsius converter")
f = int(input("Please enter Farenheit: "))

c = (f - 32)* 5.0/9

print("%i F is %.2f C" %(f,c))


import sys
f = float(sys.argv[1])
c = (f - 32)* 5.0/9

print("%i F is %.2f C" %(f,c))
"""
infile = open('farenheit.txt','r')
infile.readline()
infile.readline()
f = []
for line in infile:
    faren = line.split()
    f.append(faren[2])
    number = [float(w) for w in f]
    f.append(number)
    no = f[1][0]
    c = (f - 32)* 5.0/9
    print (no)
