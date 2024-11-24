'''Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate of Rs.
12.00 per hour for every hour worked above 40 hours. Assume that employees do not work for
fractional part of an hour.'''

for i in range(1,11):
    hours=int(input("Enter hours worked: "))
    if hours>40:
        pay=(hours-40)*12
    else:
        pay=0
    print("Overtime pay for employee",i,"is Rs.",pay)