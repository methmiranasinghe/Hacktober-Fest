def greet(name):
    """Function to greet the user."""
    try:
        if name.isalpha():
            return f"Hello, {name}!"
        else:
            raise ValueError("Invalid input. Please enter a valid name.")
    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting_message = greet(user_name)
    print(greeting_message)
