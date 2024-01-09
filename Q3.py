import math
#1.
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
x = float(input("x = "))
print(a, b, c, x)
#2.
print( "S1 = " , a*x**2 + b*x + c) 
#3.
S2 = b**2 - 4*a*c
if S2 > 0:
    print(math.sqrt(S2))
else:
    S2 = 0
    print(S2)
#4.
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if (a + b > c and a + c > b and b + c > a):
    p = 1/2 *(a + b + c)
    S1 = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(S1)
else:
    print("a, b, c are not side of a triangle")





