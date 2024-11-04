'''Enter m:10
Enter n: 2
No. of days:  5'''

m=int(input("Enter m:"))
n=int(input("Enter n: "))
days=0
while m>0:
    m=m-n
    days+=1
print("No. of days: ",days)