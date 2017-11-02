 
infile = open('farenheit.txt','r')
for i in range(3):
     infile.readline()
for line in infile:
    f = float(line.split()[-1])
    c = (f - 32)* 5.0/9
    print("%i F is %.2f C" %(f,c))
infile.close()
