'''Write a program to find the factorial value of any number entered through the keyboard'''

n=int(input("Enter a number: "))
fact=1
for i in range(1, n+1):
    fact=fact*i
print("Factorial is: ",fact)