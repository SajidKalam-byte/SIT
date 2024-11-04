'''Enter range : 5
Reverse Factorial is:  120'''
n=int(input("Enter range :"))
totl=1
while n>0:
    totl=totl*n
    n=n-1
print("Reverse Factorial is: ",totl)