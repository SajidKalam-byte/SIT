'''Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each
digit of the number is equal to the number itself, then the number is called an Armstrong number.
For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )'''

for i in range(1,501):
    sum=0
    a=i
    while(i>0):
        b=i%10
        sum=sum+b*b*b
        i=i//10
    if(a==sum):
        print(a)