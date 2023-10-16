import random

def get_random_greeting():
    """Function to get a random greeting message."""
    greetings = ["Hello", "Hi there", "Hey", "Greetings"]
    return random.choice(greetings)

def greet_user():
    """Function to greet the user with a random message."""
    user_name = input("Enter your name: ")
    random_greeting = get_random_greeting()
    return f"{random_greeting}, {user_name}!"

if __name__ == "__main__":
    greeting_message = greet_user()
    print(greeting_message)
