import mysql.connector
import bcrypt
from datetime import datetime

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="*****",
        database="bankdb"
    )

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_number INT PRIMARY KEY AUTO_INCREMENT,
        user_id VARCHAR(50),
        account_type VARCHAR(50) NOT NULL,
        balance DOUBLE DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(username)
    );
    ''')

    cursor.execute('''
    ALTER TABLE accounts AUTO_INCREMENT=5432125;
''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INT AUTO_INCREMENT PRIMARY KEY,
        account_number INT,
        type VARCHAR(50) NOT NULL,
        amount DOUBLE NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (account_number) REFERENCES accounts(account_number)
    );
    ''')
    
    conn.commit()
    conn.close()




