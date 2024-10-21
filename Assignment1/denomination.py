'''A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn
is input through the keyboard in hundreds, find the total number of currency notes of each
denomination the cashier will have to give to the withdrawer.'''

amt=int(input("Enter Amount: "))
hundreds=amt//100
fifties=(amt%100)//50
tens=(amt%100)%50//10
print("No. of 100s: ",hundreds)
print("No. of 50s: ",fifties)
print("No. of 10s: ",tens)