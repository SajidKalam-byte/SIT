'''Given the coordinates (x, y) of a center of a circle and it’s radius, write a program which will
determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use
sqrt( ) and pow( ) functions)'''
import math
cx, cy = map(int, input("Enter circle center coordinates (x y): ").split())
radius = float(input("Enter circle radius: "))
x, y = map(int, input("Enter point coordinates (x y): ").split())
distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
if distance < radius:
    print("Point is inside the circle")
elif distance == radius:
    print("Point is on the circle")
else:
    print("Point is outside the circle")
