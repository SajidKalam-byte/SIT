'''When interest compounds q times per year at an annual rate of r % for n years, the principle p 
compounds to an amount a as per the following formula. Write a program to read 10 sets of p, r, 
n & q and calculate the corresponding as. 𝐴=𝑃(1+𝑟/𝑛)^𝑛𝑡
'''
for i in range(1,11):
    p = float(input("Enter principal amount: "))
    q = int(input("Enter number of times interest is compounded per year: "))
    r = float(input("Enter rate of interest (in %): "))
    n = int(input("Enter number of years: "))
    a = p * (1 + r / (100 * q)) ** (q * n)
    print("Compound interest is: ", a.__round__(2))
