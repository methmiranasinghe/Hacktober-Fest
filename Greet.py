def greet(name):
    """Function to greet the user."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting_message = greet(user_name)
    print(greeting_message)
