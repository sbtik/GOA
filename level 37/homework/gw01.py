accounts = {}
passwords = {}






def create_account():
    name = input("Enter your name: ")

    if name in accounts:
        print("Account already exists")
    else:
        password = input("Enter your password: ")
        accounts[name] = 0
        
        passwords[name] = password
        print(f"Account created for {name}")



def verify_password(name):
    if name in passwords:
        entered_password = input("Enter your password: ")
        if passwords[name] == entered_password:
            return True
        else:
            print("Invalid Password!")
            return False
    else:
        print("Account does not exist")
        return False

def deposit():
    name = input("Enter your name: ")
    if verify_password(name):
        amount = int(input("Enter Deposit Amount: "))
        if amount >= 0:
            accounts[name] += amount
            
            print(f"Deposit Successful. New balance: {accounts[name]}")
        else:
            print("Invalid deposit amount")


def bitcoin_change():
    name = input("Enter your name: ")
    if verify_password(name):
        amount = int(input("Enter Bitcoin Amount: "))
        if amount >= 0:
            accounts[name] += amount * 10000
            print(f"Bitcoin deposit successful. New balance: {accounts[name]}")
        else:
            print("Invalid Bitcoin deposit amount")




def withdraw():
    name = input("Enter your name: ")
    if verify_password(name):
        amount = int(input("Withdraw Amount: "))
        if 0 < amount <= accounts[name]:
            accounts[name] -= amount
            print(f"Withdrawal Successful. New balance: {accounts[name]}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

def check_balance():
    name = input("Enter your name: ")
    if verify_password(name):
        print(f"Your balance: {accounts[name]}")

def transfer():
    sender = input("Enter your name: ")
    if verify_password(sender):
        receiver = input("Enter Receiver's Name: ")
        if receiver in accounts:
            amount = int(input("Enter Transfer Amount: "))
            if 0 < amount <= accounts[sender]:
                accounts[sender] -= amount
                accounts[receiver] += amount
                print(f"Transfer Successful. New balance for {sender}: {accounts[sender]}, New balance for {receiver}: {accounts[receiver]}")
            else:
                print("Invalid transfer amount or insufficient funds")
        else:
            print("Receiver's account does not exist")

def Transfer_bitcoins():
    sender = input("enter your name:")
    if verify_password(sender):
        receiver = input("Enter Receiver's Name: ")
        if receiver in accounts:
            amount = int(input("Enter Bitcoin Transfer Amount: "))
            if 0 < amount <= accounts[sender]:
                accounts[sender] -= amount * 10000
                accounts[receiver] += amount * 10000
                print(f"Bitcoin Transfer Successful. New balance for {sender}: {accounts[sender]}, New balance for {receiver}: {accounts[receiver]}")
            else:
                print("Invalid Bitcoin transfer amount or insufficient funds")
        else:
            print("Receiver's account does not exist")
    

def show_your_bitcoins():
    name = input("Enter your name: ")
    if verify_password(name):
        print(f"Your Bitcoin balance: {accounts[name]/10000}")




def main():
    while True:
        print("Welcome to Livebank  ")
        print("1. Create Account ")
        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Check Balance ")
        print("5. Transfer ")
        print("6. Show  bitcoins ")
        print("7. Bitcoin Deposit ") 
        print("8. Exit ")


        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            transfer()
        elif choice == 6:
            show_your_bitcoins()
        elif choice == 7:
            bitcoin_change()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()