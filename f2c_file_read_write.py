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
outfile = open('new_Fdeg.dat','w')
outfile.write("  F       C\n")
for i,j in zip(fdeg,cdeg):
    outfile.write("%2.2f    %2.2f"%(i,j))
    outfile.write('\n')
outfile.close()
