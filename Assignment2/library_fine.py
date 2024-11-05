'''A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for
6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30
days your membership will be cancelled. Write a program to accept the number of days the
member is late to return the book and display the fine or the appropriate message.'''

days=int(input("Enter the number of days: "))
fine=0.0
if days<=5:
    fine=days*0.50
elif days<=10:
    fine=5+(days-5)*1
elif days>10:
    fine=5+(10-5)*1+(days-10)*5
if days>30:
    print("Your membership is cancelled")
else:   
    print("Your fine is: Rs",fine)