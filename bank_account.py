from database import *

class Account:
    def __init__(self, username, account_type, account_id= None):
        self.username = username
        self.account_type = account_type
        self.account_id = account_id
        self.balance = 0
    
    def create_account(self):
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO accounts (user_id, account_type, balance) VALUES (%s, %s, %s)', 
                       (self.username, self.account_type, self.balance))
        conn.commit()
        account_id = self.get_account_id()
        print(f"Account created Successfully.\nYour Account Number is: {account_id}")
        conn.close()

    def deposit(self, amount):
        self.balance = self.get_balance() + amount
        self.update_balance(self.account_id)
        self.record_transaction('deposit', amount)
    
    def withdraw(self, amount):
        if self.get_balance() >= amount:
            self.balance = self.get_balance() - amount
            self.update_balance(self.account_id)
            self.record_transaction('withdrawal', amount)
        else:
            print('Insufficient funds.')

    def update_balance(self, account_id):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute('UPDATE accounts SET balance = %s WHERE user_id = %s AND account_number = %s',
                       (self.balance, self.username, account_id))
        
        conn.commit()
        conn.close()

    def get_balance(self):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT balance FROM accounts WHERE user_id = %s AND account_number = %s',
                       (self.username, self.get_account_id()))
        balance = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return balance

    def record_transaction(self, trans_type, amount):
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO transactions (account_number, type, amount) VALUES (%s, %s, %s)', 
                       (self.get_account_id(), trans_type, amount))
        conn.commit()
        conn.close()
    
    def get_account_id(self):
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT account_number FROM accounts WHERE user_id = %s AND account_type = %s', 
                       (self.username, self.account_type))
        account_id = cursor.fetchone()[0]
        
        conn.close()
        return account_id

class SavingsAccount(Account):
    def __init__(self, username):
        super().__init__(username, 'savings')

class CurrentAccount(Account):
    def __init__(self, username):
        super().__init__(username, 'current')

class SalaryAccount(Account):
    def __init__(self, username):
        super().__init__(username, 'salary')


class Bank:
    @staticmethod
    def get_account_details(username):
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM accounts WHERE user_id = %s', (username,))
        accounts = cursor.fetchall()
        
        for account in accounts:
            print(f"Account ID: {account[0]}, Type: {account[2]}, Balance: {account[3]}")
        
        conn.close()

    @staticmethod
    def get_transaction_history(account_id):
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM transactions WHERE account_number = %s', (account_id,))
        transactions = cursor.fetchall()
        
        for transaction in transactions:
            print(f"Transaction ID: {transaction[0]}, Type: {transaction[2]}, Amount: {transaction[3]}, Date: {transaction[4]}")
        
        conn.close()
