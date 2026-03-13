class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        """Method to display balance"""
        print(f"Dear {self.owner}, your balance is: {self.balance}")    

    def deposit(self, amount):
        """Deposit method"""
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw method"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds on the account!")

    def transfer(self, target_account, amount):
        """Method to transfer money to another BankAcount object"""
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Succesfully transferred {amount} to {target_account.owner}.")
            print(f"Your remaining balance: {self.balance}")
        else: 
            print("Transfer failed. Insufficient funds.")


account_andrii= BankAccount("Andrii", 1000)
account_alina = BankAccount("Alina", 2000)
account_mots = BankAccount("Mots", 3000)

accounts = {
    'alina': account_alina,
    'mots': account_mots,
    'andrii': account_andrii,
}


active_flag = True
while active_flag:
    answer = input("Choose your action: \n\t1.Balance \n\t2.Withdraw \n\t3.Deposit \n\t4.Transfer \n").lower()

    if answer == "1" or answer == "balance":
        account_andrii.show_balance()
        print("\n")
    
    elif answer == "2" or answer == "withdraw":
        try:
            amount = float(input("How much do u want withdraw? "))
            account_andrii.withdraw(amount)
            print("\n")
        except ValueError:
            print("Enter valid number")
    
    elif answer == "3" or answer == "deposit":
        try:
            amount = float(input("How much do u want deposit?: "))
            account_andrii.deposit(amount)
            print("\n")
        except ValueError:
            print("Enter valid number")

    elif answer == "4" or answer == "transfer":
        try:
            name = input("Enter person name: ").lower()
            if name in accounts:
                target = accounts[name]
                amt = float(input(f"Enter amount to transfer to {name.title()}: "))
                account_andrii.transfer(target, amt)
            else:
                print(f"{name.title()} not found!")
        except ValueError:
            print("Enter valid number")


    prompt = input("Do u want to continue? (y/n): ").lower()
    
    if prompt != "y":
        active_flag = False
    else:
        print("Invalid input, try again")


account_alina.balance()