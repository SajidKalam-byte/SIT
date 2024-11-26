'''If a five-digit number is input through the keyboard, write a program to print a new number
by adding one to each of its digits. For example if the number that is input is 12391 then the
output should be displayed as 23402'''


number = input("Enter a five-digit number: ")
new_number = ""


for digit in number:
    new_digit = (int(digit) + 1) % 10  
    new_number += str(new_digit)  


print(f"The new number is: {new_number}")