'''Two numbers are input through the keyboard into two locations C and D. Write a program to
interchange the contents of C and D.'''
c=(int(input("Enter a number: ")))
d=(int(input("Enter second number: ")))
c,d=d,c
print("Content of C is now : ",c)
print("Content of D is now : ",d)
