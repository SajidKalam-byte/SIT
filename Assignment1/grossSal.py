'''Rameshs basic salary is input through the keyboard. His dearness allowance is 40% of basic
salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross
salary.'''


bs=int(input("Enter basic salary: "))
da=bs*40/100
hra=bs*20/100
gs=bs+da+hra
print("Gross salary is: ",gs)
