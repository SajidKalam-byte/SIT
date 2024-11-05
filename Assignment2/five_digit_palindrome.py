'''A five-digit number is entered through the keyboard. Write a program to obtain the reversed
number and to determine whether the original and reversed numbers are equal or not.'''
num=int(input("Enter a number: "))
sum=0
a=num
while(num>0):
    b=num%10
    sum=sum*10+b
    num=num//10
if(a==sum):
    print("Palindrome")
else:
    print("Not a palindrome")