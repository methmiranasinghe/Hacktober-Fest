def authenticate_user():
    """Function to authenticate the user."""
    allowed_username = "user123"
    allowed_password = "password123"
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == allowed_username and password == allowed_password:
        return True
    else:
        return False

def greet_user():
    """Function to greet the authenticated user."""
    user_name = input("Enter your name: ")
    return f"Hello, {user_name}!"

if __name__ == "__main__":
    if authenticate_user():
        greeting_message = greet_user()
        print(greeting_message)
    else:
        print("Authentication failed. Access denied.")

