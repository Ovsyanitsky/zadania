from math import sqrt
def area(a,b,c):
    p2 = (a + b + c) / 2
    return sqrt(p2 * (p2 - a) * (p2 - b) * (p2 - c))
a = int(input())
b = int(input())
c = int(input())
print(area(a,b,c))
    
