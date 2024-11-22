'''2. Print pascal triangle having n rows.

'''
n=7    
for i in range(n):
    a = 1
    for j in range(i + 1):
        print(a, end=" ")
        a = a * (i - j) // (j + 1)
    print()
