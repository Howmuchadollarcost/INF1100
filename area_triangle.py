"""
def area(x):
        A = 0.5*abs(x[2][0]*x[3][1]-x[3][0]*x[2][1]-x[1][0]*x[3][1]+
        x[3][0]*x[1][1]+x[1][0]*x[2][1]-x[2][0]*x[1][1])
        return A
triangle1 = {1:(1,1),2:(2,1),3:(1,3)}   #list of tuples
print(area(triangle1))

"""

def area(vertices):
    x1=vertices[0][0]
    y1= vertices[0][1]
    x2=vertices[1][0]
    y2=vertices[1][1]
    x3=vertices[2][0]
    y3=vertices[2][1]
    A = 0.5*abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
    return A
triangle = ([[1,1], [2, 1], [1,3]]) #nested lists
print (area(triangle))
