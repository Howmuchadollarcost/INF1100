infile = open('Fdeg.dat','r')
for i in range(3):
    infile.readline()
fdeg = []
cdeg = []
for line in infile:
    f = (float(line.split()[-1]))
    c = (f - 32)* 5.0/9
    fdeg.append(f)
    cdeg.append(c)
print ("f   c")
for i,j in zip(fdeg,cdeg):
    print("%2i F - %2.2f C" %(i,j))
