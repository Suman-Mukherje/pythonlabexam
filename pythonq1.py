
import datetime

class Account:

    def __init__(self, account_number, date_of_opening, balance, customer_name):
        self.account_number = account_number
        self.date_of_opening = date_of_opening
        self.balance = balance
        self.customer_name = customer_name
        self.account_history = []
        print("Account created for "+ self.customer_name+" with initial deposit "+str(self.balance)+" on "+self.date_of_opening)
        print("Account no for this customer is :"+self.account_number)

    def deposit(self, amount):
        self.balance += amount
        self.account_history.append("Deposit of $" + str(amount) + " on " + str(datetime.datetime.now()))
        print("Rs: "+str(amount)+" deposited on account no:"+self.account_number)
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.account_history.append("Withdrawal of $" + str(amount) + " on " + str(datetime.datetime.now()))
            print("Rs: "+str(amount)+"withdrawn from account no: "+self.account_number)
        
    def check_balance(self):
        print("The balance of account no: "+self.account_number+" is Rs: "+str(self.balance))

    def get_account_history(self):
        history=self.account_history
        print("Showing account history:---------")
        for h in history:
            print(h)



def Menu (acc):
    loop='Y'
    print("Bank account details of "+ str(acc.customer_name)+ " with account no "+str(acc.account_number))
    while(loop=='Y'):
        choice=input("Enter 1 for deposit,2 for withdrawn , 3 for balancecheck and 4 for accounthistory:: ")
        if choice=='1':
            am1=int(input("Enter the amount to be deposited :: "))
            acc.deposit(am1)
        elif choice=='2':
            am1=int(input("Enter the amount to be withdrawn :: "))
            acc.withdraw(am1)
        elif choice=='3':
            acc.check_balance()
        elif choice=='4':
            acc.get_account_history()
        else:
            print("Bad Choice")
        
        loop=str(input("Do you want to continue Y/N:"))
        if(loop!='Y'):
            print("Ok ! The details of this user completed")
    
        
    
acc1 = Account("1234567890", "2023-07-23", 1000, "Suman Mukherjee")
Menu(acc1)
acc2 = Account("1234564589", "2023-07-21", 1000, "Souvik Das")    
Menu(acc2)

