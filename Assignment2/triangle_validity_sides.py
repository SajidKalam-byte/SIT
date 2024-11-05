'''If the three sides of a triangle are entered through the keyboard, write a program to check
whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater than
the largest of the three sides.'''

side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))
if side1 + side2 > side3 or side1 + side3 > side2 or side2 + side3 > side1:
    print("Triangle is valid")
else:
    print("Triangle is not valid")
