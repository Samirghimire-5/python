# SAMIR_RONISH_SAMYAM_SHRIYASH
# TSCSG144882, TSCJM132682, TSCSP145382, TSCSS147382

users = {"admin": "pass123", "guest": "welcome", "user1": "p@ssword"}

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print("\n--- Role-Based Login System ---")
    print("1. Role 1 (Admin)")
    print("2. Role 2 (Guest)")
    print("3. Role 3 (User)")
    print("4. Exit")

    choice = input("Select a role (1-4): ")

    if choice == "4":
        print("Exiting program. Goodbye!")
        break

    if choice in ["1", "2", "3"]:
        user_input = input("Enter Username: ")
        pass_input = input("Enter Password: ")

        # check if user name exists in user dictionary and matches the password
        if user_input in users and users[user_input] == pass_input:
            print("\nLogin Successful - Welcome to the System")
            break  # stop loop cause login successful
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Invalid credentials! Attempts remaining: {remaining}")
    else:
        print("Invalid choice, please select 1-4.")

# terminate program
if attempts == max_attempts:
    print("\nToo many failed attempts. The program is now terminating.")
