class BankAccount: 
    def __init__(self, owner, balance=0): 
        self.owner = owner 
        self.balance = balance 

    def deposit(self, amount): 
        self.balance += amount 
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount): 
        if amount <= self.balance: 
            self.balance -= amount 
            print(f"Withdrew: {amount}. Remaining Balance: {self.balance}")
        else: 
            print("Transaction Failed: Insufficient balance")
            
account = BankAccount("John", 1000) 

# 2. Add 500
account.deposit(500) 

# 3. Take out 300
account.withdraw(300) 

# 4. Check the final amount
print(f"Final Balance for {account.owner}: {account.balance}")


def display_info(self):
    print("-" * 20)
    print(f"Account Holder: {self.owner}")
    print(f"Current Balance: ${self.balance:,.2f}")
    print("-" * 20)