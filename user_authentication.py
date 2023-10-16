def authenticate_user():
    """Function to authenticate the user."""
    allowed_users = {
        "user123": "password123",
        "user5420": "password123"
    }

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in allowed_users and password == allowed_users[username]:
        return True
    else:
        return False

# Example of using the function
if authenticate_user():
    print("Authentication successful")
else:
    print("Authentication failed")

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

