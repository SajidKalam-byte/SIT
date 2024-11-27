'''Write a program to print all prime numbers from 1 to 300. (Hint: Use nested loops, break and 
continue) '''
for i in range(1,301):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)