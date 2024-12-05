class Account:
    def deposit(self):
        
        amt=int(input("Enter amount: "))
        self.balance=self.balance+amt

    def Open_Account(self):
        self.acc_no=1151205
        self.balance=0
    def Balance_Enquiry(self):
        print("Balance is: ",self.balance)
        print("Account Number is: ",self.acc_no)

ac=Account()
ac.Open_Account()
ac.Balance_Enquiry()
ac.deposit()
ac.Balance_Enquiry()