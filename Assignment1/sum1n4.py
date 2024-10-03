'''If a four-digit number is input through the keyboard, write a program to obtain the sum of the
first and last digit of this number.'''
num=(int(input("Enter a number: "))) #1234
sum=0
a=num%10 ##4
b=num//1000
sum=a+b
print("Sum of 1st and 4th digits is: ",sum)