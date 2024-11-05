'''Find the absolute value of a number entered through the keyboard.'''
num=int(input("Enter a number: "))
if num<0:
    num=num*-1
print("Absolute value is: ",num)