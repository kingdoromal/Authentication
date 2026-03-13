import sqlite3

def login(username, password):
    try:

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))

        user = cursor.fetchone()

        if user:
            print("Login successful!")
        else:
            print("Invalid username or password.")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        conn.close()
username = input("Enter username: ")
password = input("Enter password: ")

login(username, password)
