from database import *


class User:
    @staticmethod
    def create_user(username, password):
        conn = create_connection()
        cursor = conn.cursor()
        
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_pw))
            conn.commit()
        except mysql.connector.IntegrityError:
            print('Username already exists.')
        finally:
            conn.close()

    @staticmethod
    def authenticate_user(username, password):
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT password FROM users WHERE username = %s', (username,))
        record = cursor.fetchone()
        
        if record and bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()):
            print('Authentication successful.')
            conn.close()
            return True
        else:
            print('Authentication failed.')
            conn.close()
            return False
        
