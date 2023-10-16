def greet_users_from_file(file_path):
    # Open the file for reading
    try:
        with open("username.txt", "r") as file:
        # Read the lines from the file
            lines = file.readlines()

        # Loop through each line (each username) and greet them
            for line in lines:
                username = line.strip()  # Remove any leading/trailing whitespace
                if username:
                    print(f"Hello, {username}!")

    except FileNotFoundError:
        print("File 'username.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

