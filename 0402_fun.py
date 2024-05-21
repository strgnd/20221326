import math

def cir_area(r):
    c_area = math.pi * r * r
    return c_area

def cir_circum(r):
    c_circum = 2 * math.pi * r
    return c_circum

sub_area = cir_area(3.5)
sub_circum = cir_circum(3.5)

print("%.1f" %sub_area)
print("%.1f" %sub_circum)