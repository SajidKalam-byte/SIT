'''An Insurance company follows following rules to calculate premium.
• If a person’s health is excellent and the person is between 25 and 35 years of age and lives in
a city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot
exceed Rs. 2 lakhs.
• If a person satisfies all the above conditions except that the sex is female then the premium is
Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
• If a person’s health is poor and the person is between 25 and 35 years of age and lives in a
village and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs.
10,000.
• In all other cases the person is not insured.
Write a program to output whether the person should be insured or not, his/her premium rate and
maximum amount for which he/she can be insured.'''

age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").lower()
city = input("Belong to city (Y/N): ").lower()
health = input("Enter health condition Excellent(E) or Poor(P): ").lower()

if health == "e" and 25 <= age <= 35 and city == "y":
    if gender == "m":
        print("Premium is Rs. 4 per thousand; Maximum policy amount is Rs. 2 lakhs")
    elif gender == "f":
        print("Premium is Rs. 3 per thousand; Maximum policy amount is Rs. 1 lakh")
    else:
        print("Not insured")
elif health == "p" and 25 <= age <= 35 and city == "n" and gender == "m":
    print("Premium is Rs. 6 per thousand; Maximum policy amount is Rs. 10,000")
else:
    print("Not insured")
