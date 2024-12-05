class Account():
    count=0
    def __init__(self):
        Account.count+=1
        self.acc_no=Account.count
        self.balance=0

    def __del__(self):
        Account.count-=1

    def Balance_Enquiry(self):
        print(self.acc_no)
        print(self.balance)

    def Deposit(self,amt):
        self.balance+=amt
    
    def Withdraw(self,amt):
        self.balance-=amt
        ac1.Balance_Enquiry()

ac1=Account()
ac1.Balance_Enquiry()
ac2=Account()
ac2.Balance_Enquiry()

ac1.Deposit(1500)
ac1.Withdraw(500)

ac2.Deposit(1000)
ac2.Withdraw(500)




