def greet(name):
    """Function to greet the user."""
    # Check if the input is empty or contains only whitespace
    if not name.strip():
        return "Invalid input. The name field can not be empty."

    # Check if the input contains only alphabetic characters
    if name.isalpha():
        return f"Hello, {name.strip()}!"
    else:
        return "Invalid input. Please enter a valid name."
