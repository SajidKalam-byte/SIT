x=float(input("Enter centre for x: "))
y=float(input("Enter centre for y: "))
x1=float(input("Enter coordinate for x1: "))
y2=float(input("Enter coordinates for y1: "))
r=float(input("Enter radius: "))
d=(x-x1)**2+(y-y2)**2
a=r**2
if a> d:
    print(" Inside the circle ")
elif a==2:
    print("On the circle ")
else:
    print("Outside the circle")