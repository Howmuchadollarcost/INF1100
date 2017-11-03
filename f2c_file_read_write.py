"""
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
"""

def f_deg(degrees):
    return (degrees - 32)* 5.0/9
infile = open('Fdeg.dat','r')
for i in range (3):
    infile.readline()
fdeg = [];cdeg = []
for line in infile:
    f = float((line.split()[-1]))
    fdeg.append(f)
for f in fdeg:
    cdeg.append(f_deg(f))
with open('new_Fdeg2.dat', 'w') as outfile:
    outfile.write("-----------\n")
    outfile.write("   f    c   \n")
    outfile.write("-----------\n")
    for i in range(len(fdeg)):
        outfile.write("%6.2f %6.2f\n" %(fdeg[i],cdeg[i]))
