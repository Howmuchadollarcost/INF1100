
def H(x):
    if x >= 0:
        return 1
    else:
        return 0

x = [-10,-10e-15,0,10e-15,10]
def test_H():
    for i in x:
        print (" %5.1f  %5.1f " %(i,H(i)))
test_H()

"""
def H(x):
    try:
        assert type(x) in (int,float)
        if x >= 0:
            return 1
        else:
            return 0
    except AssertionError:
        return "Not a real number!"

x = [-10,-10e-15,0,10e-15,10]
def test_H():
    for i in x:
        print (" %5.1f  %5.1f " %(i,H(i)))
test_H()
"""
