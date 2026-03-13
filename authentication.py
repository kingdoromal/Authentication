import hashlib

# Simulated database (username: hashed_password)
users_db = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "user": hashlib.sha256("password".encode()).hexdigest()
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    try:
        # Input validation
        if not username or not password:
            return "Error: Username and password cannot be empty."

        if username not in users_db:
            return "Authentication failed: User not found."

        hashed_input = hash_password(password)

        if users_db[username] == hashed_input:
            return "Login successful!"
        else:
            return "Authentication failed: Incorrect password."

    except Exception as e:
        return f"Error occurred: {str(e)}"

# Login process
print("=== Login System ===")

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

result = authenticate(username, password)
print(result)
