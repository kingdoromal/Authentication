import re

def validate_username(username):
    if not username:
        return "Username cannot be empty."
    
    if len(username) < 4:
        return "Username must be at least 4 characters."
    
    if not username.isalnum():
        return "Username must contain only letters and numbers."
    
    return "Valid"

def validate_password(password):
    if not password:
        return "Password cannot be empty."
    
    if len(password) < 6:
        return "Password must be at least 6 characters."
    
    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    
    if not re.search("[0-9]", password):
        return "Password must contain at least one number."
    
    return "Valid"

# Input
username = input("Enter username: ")
password = input("Enter password: ")

# Validation
user_check = validate_username(username)
pass_check = validate_password(password)

if user_check != "Valid":
    print("Username Error:", user_check)
elif pass_check != "Valid":
    print("Password Error:", pass_check)
else:
    print("Input is valid. You may proceed with authentication.")
