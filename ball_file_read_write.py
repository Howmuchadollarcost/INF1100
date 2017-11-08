
def read_file(file):
    t = []
    temp_t =[]
    with open(file,'r') as infile:
        line = infile.readline()
        v0 = (float(line.split()[1]))
    with open(file,'r') as infile2:
        for i in range(2):
            x = infile2.readline()
        for line in infile2:
            temp_t.append((line.split()))
    x = [t.append((float(j))) for i in temp_t for j in i]
    return sorted(t),v0

file_in = read_file('v0_and_t.dat')

t = file_in[0]
v0 = file_in[1]


def y_pos(v0,t,g=9.81):
    return v0*t-0.5*g*t**2

def write_file(file):
    with open(file ,'w') as outfile:
        outfile.write("---------------\n")
        outfile.write(" t        y    \n")
        outfile.write("---------------\n")
        for i in range(21):
            outfile.write("%6.4f %6.4f\n"%(t[i],y_pos(v0,t[i])))
            #print(t[i],y_pos(v0,t[i]))
write_file("formatted_v0_and_t.dat")


def test(file_in,file_out):
    x = read_file(file_in)
    y = write_file(file_out)
    return y
test("v0_and_t.dat","test_1.txt")

"""
def read(file):
    t = []
    cnt = 0
    for line in file:
        if cnt == 0:
            v = line.split()
            v0 = float(v[1])
        elif cnt > 1:
            t.append([float(i) for i in line.split()])
        cnt += 1
    f_t = [j for i in t for j in i]
    return v0,f_t
file = open("v0_and_t.dat")

def y_pos(v0,t,g=9.81):
    return v0*t-0.5*g*t**2

def write_file(file):
    with open(file ,'w') as outfile:
        outfile.write("---------------\n")
        outfile.write(" t        y    \n")
        outfile.write("---------------\n")
        for i in range(21):
            outfile.write("%6.3f %6.3f\n"%(t[i],t[i]*v0))
    return file
"""
