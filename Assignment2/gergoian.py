'''According to the Gregorian calendar, it was Monday on the date 01/01/1900. If any year is
input through the keyboard write a program to find out what is the day on 1 st January of this
year.'''
year = int(input("Enter year: "))
days = (year - 1900) * 365 + (year - 1900) // 4
day_of_week = days % 7
if day_of_week == 0:
    print("Monday")
elif day_of_week == 1:
    print("Tuesday")
elif day_of_week == 2:
    print("Wednesday")
elif day_of_week == 3:
    print("Thursday")
elif day_of_week == 4:
    print("Friday")
elif day_of_week == 5:
    print("Saturday")
else:
    print("Sunday")
