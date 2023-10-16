def greet_users_from_file(file_path):
    """Function to greet users listed in a file."""
    try:
        with open(file_path, 'r') as file:
            users = file.readlines()
            for user in users:
                print(f"Hello, {user.strip()}!")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the file containing user names: ")
    greet_users_from_file(file_path)
