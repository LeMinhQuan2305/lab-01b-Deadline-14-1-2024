#1

a = int(input("number1 = "))
b = int(input("number2 = "))
print("The multiplication result is ", a*b)
print("The sum result is ", a+b)

#2
n = int(input("Printing current and previous number sum in a range: "))
sum = 0

for i in range(n):
    a = i -1
    if a < 0:
        a = 0
    print("Current Number ", i, "Previous Number  ", a, "  Sum:  ", a + i)

#3
print("Name", "is", "James", sep="**")

#Q4
a= int(input())
b= int(input())
c= int(input())


print("The octal number of decimal number", a, "is", oct(a) )
print("The octal number of decimal number", b, "is", oct(b) )
print("The octal number of decimal number", c, "is", oct(c) )
num = float(input())
print("{:.2f}".format(num))