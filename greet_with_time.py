import datetime

def greet_with_time(name):
    """Function to greet the user based on the time of day."""
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12):
        return f"Good morning, {name}!"
    elif current_time < datetime.time(17):
        return f"Good afternoon, {name}!"
    else:
        return f"Good evening, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting_message = greet_with_time(user_name)
    print(greeting_message)
