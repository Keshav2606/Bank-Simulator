from database import *
from users import *
from bank_account import *

def main():
    create_tables()

    while True:
        print("1. Create User")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            User.create_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if User.authenticate_user(username, password):
                user_id = username
                while True:
                    print("1. Create Savings Account")
                    print("2. Create Current Account")
                    print("3. Create Salary Account")
                    print("4. Deposit")
                    print("5. Withdraw")
                    print("6. View Account Details")
                    print("7. View Transaction History")
                    print("8. Logout")
                    choice = input("Enter choice: ")
                    
                    if choice == '1':
                        account = SavingsAccount(user_id)
                        account.create_account()
                    elif choice == '2':
                        account = CurrentAccount(user_id)
                        account.create_account()
                    elif choice == '3':
                        account = SalaryAccount(user_id)
                        account.create_account()
                    elif choice == '4':
                        account_id = input("Enter account ID: ")
                        account_type = input("Enter account type: ").lower()
                        amount = float(input("Enter amount: "))
                        account = Account(user_id, account_type, account_id)
                        account.deposit(amount)
                    elif choice == '5':
                        account_id = input("Enter account ID: ")
                        account_type = input("Enter account type: ").lower()
                        amount = float(input("Enter amount: "))
                        account = Account(user_id, account_type, account_id)
                        account.withdraw(amount)
                    elif choice == '6':
                        Bank.get_account_details(user_id)
                    elif choice == '7':
                        account_id = input("Enter account ID: ")
                        Bank.get_transaction_history(account_id)
                    elif choice == '8':
                        break
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
