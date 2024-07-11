**Banking Simulator**
This is a CLI based banking simulator written in Python. It allows user authentication, creation of different types of bank accounts, performing transactions, and retrieving account details. The application connects to a MySQL database to store user and account information.

**Prerequisites**
1. Python 3.x
2. MySQL server
3. MySQL Connector/Python (mysql-connector-python)
4. bcrypt library for password hashing

**Database Setup**
1. Create the MySQL Database "bankdb"

2. Open the MySQL command-line client or MySQL Workbench and execute the following SQL commands to create the database:

    CREATE DATABASE IF NOT EXISTS bankdb;
    USE bankdb;

**Create a MySQL User and Grant Privileges**

1. Create a MySQL user and grant the necessary privileges. Replace 'your_password' with a strong password.

    CREATE USER 'root_user'@'localhost' IDENTIFIED BY 'your_password';
    GRANT ALL PRIVILEGES ON banking_simulator.* TO 'root_user'@'localhost';
    FLUSH PRIVILEGES;

**Update Database Connection Settings**

1. In the Python script, update the "create_connection()" function with the correct MySQL user and password:

    def create_connection():
        conn = mysql.connector.connect(
            host="localhost",
            user="root_user",
            password="your_password",
            database="bankdb"
        )
        return conn

**Running the Program**
1. Run the Python File "main.py"

**Usage**
1. Create a User
    Follow the on-screen prompts to create a new user.

2. Login
    Login with your username and password.

3. Perform Banking Operations
    After logging in, you can create savings or checking accounts, deposit or withdraw money, and view account details and transaction history.

4. Logout
    Choose the logout option to return to the main menu.
