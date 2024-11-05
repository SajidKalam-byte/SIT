'''Given a point (x, y), write a program to find out if it lies on the x-axis, y-axis or at the origin,
viz. (0, 0)'''
x, y = map(int, input("Enter point coordinates (x y): ").split())
if x == 0 and y == 0:
    print("Point is at the origin")
elif x == 0:
    print("Point lies on the y-axis")
elif y == 0:
    print("Point lies on the x-axis")
else:
    print("Point is not on any axis")
