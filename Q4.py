a = float(input())
b = float(input())
c = float(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > c:
    a, c = c, a
print("max =", a)
print("min =", c)
print(a, b, c)