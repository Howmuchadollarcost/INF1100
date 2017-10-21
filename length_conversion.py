"""
1.4 Convert from meter to British length units

1 inch = 2.54 cm
1 foot = 12 inches
1 yard = 3 feet
1 mile = 1760 yards
"""

def length_conversion(l): #length given in meter
    cm = 100*l
    inch = cm/2.54
    foot = inch/12
    yard = foot/3
    mile = yard/1760
    return l,cm,inch,foot,yard,mile


x = length_conversion(float(input("Sett inn meter: ")))
print ("%d m tilsvarer: %d cm, %.2f inch, %.2f inch,%.2f yard og %.3f mil" %(x))
