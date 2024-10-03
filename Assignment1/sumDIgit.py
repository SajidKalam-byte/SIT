'''Two numbers are input through the keyboard into two locations C and D. Write a program to
interchange the contents of C and D.'''
num=(int(input("Enter a number: ")))
sum=0
while(num>0):
    a=num%10
    sum=sum+a
    num=num//10
print("Sum of digits is: ",sum)