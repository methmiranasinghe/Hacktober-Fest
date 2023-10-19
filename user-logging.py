import logging

# Configure logging
logging.basicConfig(filename='user_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def log_user_interaction(user_input):
    logging.info('User interaction: {}'.format(user_input))

def log_error(error_message):
    logging.error('Error: {}'.format(error_message))

def main():
    print("Welcome to the User Logging App!")
    while True:
        user_input = input("Enter your input (type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        try:
            # Some processing
            result = 10 / int(user_input)
            print("Result: {}".format(result))
            log_user_interaction(user_input)
        except ValueError as e:
            print("Invalid input. Please enter a number.")
            log_error(str(e))
        except ZeroDivisionError as e:
            print("Cannot divide by zero.")
            log_error(str(e))

if __name__ == "__main__":
    main()
