def greet(name):
    """Function to greet the user."""
    try:
        if name.strip().isalpha():
            return f"Hello, {name.strip()}!"
        else:
            raise ValueError("Invalid input. Please enter a valid name.")
    except ValueError as e:
        return str(e)

