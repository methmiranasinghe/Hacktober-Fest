def greet(name):
    """Function to greet the user."""
    if name.strip().isalpha():
        return f"Hello, {name.strip()}!"
    else:
        return "Invalid input. Please enter a valid name."

