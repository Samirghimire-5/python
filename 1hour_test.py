bank_database = {
    "Admin": [{"username": "hariKumar", "password": "Hari@123", "name": "Hari"}],
    "Staff": [
        {"username": "shyamBasnet", "password": "shyam@123", "name": "Shyam"},
        {"username": "krishnaShai", "password": "7krish@119", "name": "Krishna"},
    ],
    "Customer": [
        {
            "username": "shivaBaskota",
            "password": "shivashiva",
            "name": "Shiva",
            "balance": 50000,
        },
        {
            "username": "parvatiBudathoki",
            "password": "budayatatat",
            "name": "Parvati",
            "balance": 75000,
        },
    ],
}

roles_mapping = {"1": "Admin", "2": "Staff", "3": "Customer"}
login_attempts = 0


# functions for each operation
def add_staff():
    """Add new staff"""
    print("\n--- Add Staff ---")
    name = input("Enter name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # checking if username exists
    for staff in bank_database["Staff"]:
        if staff["username"] == username:
            print("Username already exists!")
            return

    new_staff = {"username": username, "password": password, "name": name}
    bank_database["Staff"].append(new_staff)
    print(f"Staff {name} added successfully!")


def add_customer():
    """Add new customer"""
    print("\n--- Add Customer ---")
    name = input("Enter name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    balance = float(input("Enter initial balance: "))

    # checking if username exists
    for customer in bank_database["Customer"]:
        if customer["username"] == username:
            print("Username already exists!")
            return

    new_customer = {
        "username": username,
        "password": password,
        "name": name,
        "balance": balance,
    }
    bank_database["Customer"].append(new_customer)
    print(f"Customer {name} added successfully!")


def view_all_staff():
    """View all staff"""
    print("\n--- All Staff ---")
    if not bank_database["Staff"]:
        print("No staff found.")
        return
    for i, staff in enumerate(bank_database["Staff"], 1):
        print(f"{i}. {staff['name']} (Username: {staff['username']})")


def view_all_customers():
    """View all customers"""
    print("\n--- All Customers ---")
    if not bank_database["Customer"]:
        print("No customers found.")
        return
    for i, customer in enumerate(bank_database["Customer"], 1):
        print(
            f"{i}. {customer['name']} - Balance: Rs.{customer['balance']} (Username: {customer['username']})"
        )


def search_customer():
    """Search customer by name"""
    print("\n--- Search Customer ---")
    search = input("Enter customer name to search: ").lower()
    found = False
    for customer in bank_database["Customer"]:
        if search in customer["name"].lower():
            print(f"Found: {customer['name']} - Balance: Rs.{customer['balance']}")
            found = True
    if not found:
        print("No customer found.")


def deposit_money(current_user):
    """Deposit money"""
    print("\n--- Deposit Money ---")
    if current_user["role"] == "Customer":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            current_user["balance"] += amount
            print(f"Rs.{amount} deposited successfully!")
            print(f"New balance: Rs.{current_user['balance']}")
        else:
            print("Invalid amount!")
    else:  # staff
        #find costumer
        name = input("Enter customer name: ")
        for customer in bank_database["Customer"]:
            if customer["name"].lower() == name.lower():
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    customer["balance"] += amount
                    print(f"Rs.{amount} deposited to {customer['name']}'s account!")
                    print(f"New balance: Rs.{customer['balance']}")
                else:
                    print("Invalid amount!")
                return
        print("Customer not found!")


def withdraw_money(current_user):
    """Withdraw money"""
    print("\n--- Withdraw Money ---")
    if current_user["role"] == "Customer":
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= current_user["balance"]:
            current_user["balance"] -= amount
            print(f"Rs.{amount} withdrawn successfully!")
            print(f"New balance: Rs.{current_user['balance']}")
        elif amount > current_user["balance"]:
            print("Insufficient balance!")
        else:
            print("Invalid amount!")
    else:  # staff
        # find customer
        name = input("Enter customer name: ")
        for customer in bank_database["Customer"]:
            if customer["name"].lower() == name.lower():
                amount = float(input("Enter amount to withdraw: "))
                if amount > 0 and amount <= customer["balance"]:
                    customer["balance"] -= amount
                    print(f"Rs.{amount} withdrawn from {customer['name']}'s account!")
                    print(f"New balance: Rs.{customer['balance']}")
                elif amount > customer["balance"]:
                    print("Insufficient balance!")
                else:
                    print("Invalid amount!")
                return
        print("Customer not found!")


def view_profile(current_user):
    """View profile"""
    print("\n--- My Profile ---")
    print(f"Name: {current_user['name']}")
    print(f"Username: {current_user['username']}")
    print(f"Balance: Rs.{current_user['balance']}")


def reset_password(current_user):
    """Reset password"""
    print("\n--- Reset Password ---")
    old = input("Enter current password: ")
    if old != current_user["password"]:
        print("Incorrect password!")
        return
    new = input("Enter new password: ")
    confirm = input("Confirm new password: ")
    if new == confirm:
        current_user["password"] = new
        print("Password reset successful!")
    else:
        print("Passwords don't match!")


# main program
while login_attempts < 3:
    print("\n" + "=" * 40)
    print("    BANKING SYSTEM")
    print("=" * 40)
    print("1. Admin")
    print("2. Staff")
    print("3. Customer")
    print("4. Exit")

    choice = input("Select role (1-4): ")

    if choice == "4":
        print("Goodbye!")
        break

    if choice not in roles_mapping:
        print("Invalid choice!")
        continue

    role = roles_mapping[choice]
    print(f"\n--- {role} Login ---")
    username = input("Username: ")
    password = input("Password: ")

    # authenticate
    user = None
    for u in bank_database[role]:
        if u["username"] == username and u["password"] == password:
            user = u.copy()
            user["role"] = role
            break

    if user:
        print(f"\nWelcome, {user['name']}!")
        login_attempts = 0

        # dashboard based on role
        while True:
            if role == "Admin":
                print("\n--- Admin Menu ---")
                print("1. Add Staff")
                print("2. Add Customer")
                print("3. View All Staff")
                print("4. View All Customers")
                print("5. Search Customer")
                print("6. Logout")

                opt = input("Select option: ")
                if opt == "1":
                    add_staff()
                elif opt == "2":
                    add_customer()
                elif opt == "3":
                    view_all_staff()
                elif opt == "4":
                    view_all_customers()
                elif opt == "5":
                    search_customer()
                elif opt == "6":
                    break
                else:
                    print("Invalid option!")

            elif role == "Staff":
                print("\n--- Staff Menu ---")
                print("1. View Customers")
                print("2. Search Customer")
                print("3. Deposit Money")
                print("4. Withdraw Money")
                print("5. Logout")

                opt = input("Select option: ")
                if opt == "1":
                    view_all_customers()
                elif opt == "2":
                    search_customer()
                elif opt == "3":
                    deposit_money(user)
                elif opt == "4":
                    withdraw_money(user)
                elif opt == "5":
                    break
                else:
                    print("Invalid option!")

            elif role == "Customer":
                print("\n--- Customer Menu ---")
                print("1. View Profile")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Reset Password")
                print("5. Logout")

                opt = input("Select option: ")
                if opt == "1":
                    view_profile(user)
                elif opt == "2":
                    deposit_money(user)
                elif opt == "3":
                    withdraw_money(user)
                elif opt == "4":
                    reset_password(user)
                elif opt == "5":
                    break
                else:
                    print("Invalid option!")
    else:
        login_attempts += 1
        print(f"Login failed! Attempts left: {3-login_attempts}")
        if login_attempts == 3:
            print("Too many failed attempts. Program terminated!")
