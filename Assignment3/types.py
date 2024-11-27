'''Write a program to enter the numbers till the user wants and at the end it should display the count'''
pos=0
neg=0
zeros=0
while True:
    start=(input("\n-----------------------------------------------\nPress spacebar to stop or press any key to continue\n-----------------------------------------------\n"))
    if start==" ":
        break
    else:
        n=int(input("Enter numbers : "))
        if n>0:
            print("Positive")
            pos+=1
        elif n<0:
            print("Negative")
            neg+=1
        else:
            print("Zero")
            zeros+=1
print("Positive numbers: ",pos)
print("Negative Numbers: ",neg)
print("Zeros: ",zeros)
