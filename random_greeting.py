import random

def get_random_greeting():
    """Function to get a random greeting message in different languages."""
    greetings = {
        "English": ["Hello", "Hi there", "Hey", "Greetings"],
        "Spanish": ["Hola", "Buenos días", "Saludos"],
        "French": ["Bonjour", "Salut", "Coucou"],
        "German": ["Hallo", "Guten Tag", "Grüße"],
    }
    
    language = random.choice(list(greetings.keys()))
    random_greeting = random.choice(greetings[language])
    
    return f"{random_greeting}, {language}!"

if __name__ == "__main":
    greeting_message = get_random_greeting()
    print(greeting_message)
