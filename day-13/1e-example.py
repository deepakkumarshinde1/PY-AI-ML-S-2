# Bank deposit and withdrawal.

class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def checkBalance(self):
        print(f"Hi {self.name} , your bank balance is : ₹{self.balance}/-")

    def deposit(self,amount=0):
        self.balance += amount
        print("Amount deposited successfully.")
        print(f" Your new bank  balance is ₹{self.balance}/-")

    def withdrawal(self,amount=0):
        self.balance -= amount
        print("Amount withdrawal successfully.")
        print(f" Your new bank  balance is ₹{self.balance}/-")

bank = Bank("Deepakkumar",1000)
bank.checkBalance()
bank.deposit(200)
bank.withdrawal(11000)