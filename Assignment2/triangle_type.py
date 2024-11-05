'''If the three sides of a triangle are entered through the keyboard, write a program to check
whether the triangle is isosceles, equilateral, scalene or right angled triangle.'''

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
    print("Right-angled triangle")
else:
    print("Scalene triangle")
