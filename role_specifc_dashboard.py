company_data = {
    "Boss": [{"username": "big_boss", "password": "123", "name": "Alice"}],
    "Manager": [
        {"username": "hello", "password": "456", "name": "little bigge"},
        {"username": "samir", "password": "789", "name": "hasnen"},
    ],
    "Employee": [
        {"username": "shiva", "password": "abc", "name": "karin"},
        {"username": "parvati", "password": "xyz", "name": "parvu"},
    ],
}

roles_map = {"1": "Boss", "2": "Manager", "3": "Employee"}

while True:
    print("\n--- Role-Based Login System ---")
    print("1. Boss")
    print("2. Manager")
    print("3. Employee")
    print("4. Exit")

    choice = input("Select a role (1-4): ")

    if choice == "4":
        print("Exiting program. Goodbye!")
        break

    if choice not in roles_map:
        print("Invalid choice. Please try again.")
        continue

    selected_role = roles_map[choice]
    username = input("Enter username: ")
    password = input("Enter password: ")

    # authentication logic
    user_authenticated = False
    current_user = None

    for user in company_data[selected_role]:
        if user["username"] == username and user["password"] == password:
            user_authenticated = True
            current_user = user
            break

    if user_authenticated:
        print(f"\nWelcome, {current_user['name']}! (Role: {selected_role})")

        # sub menu logic
        while True:
            print(f"\n--- {selected_role} Dashboard ---")
            if selected_role == "Boss":
                print(
                    "1. Add Manager\n2. Add Employee\n3. View Managers\n4. View Employees\n5. Search Manager or Employee\n6. Logout"
                )
            elif selected_role == "Manager":
                print(
                    "1. Add Employee\n2. View Employees\n3. Search Employee\n4. Logout"
                )
            elif selected_role == "Employee":
                print("1. View Profile\n2. Edit Profile\n3. Logout")

            sub_choice = input("Select an option: ")

            # logout logic
            if (
                (selected_role == "Boss" and sub_choice == "6")
                or (selected_role == "Manager" and sub_choice == "4")
                or (selected_role == "Employee" and sub_choice == "3")
            ):
                print("Logging out...")
                break

            # no functionality for now
            else:
                print(f"Option {sub_choice} selected. Functionality coming soon!")
    else:
        print("Login Failed! Incorrect username or password.")
