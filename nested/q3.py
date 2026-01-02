# Question 3: Login System with Security Check
# Write a Python program that:
#  Takes username and password from the user
# Rules:
# 1. If username is correct:
# o If password is correct → Login Successful
# o Else:
#  Ask for security code
#  If security code is correct → Login Successful
#  Else → Account Locked
# 2. If username is incorrect → Invalid User

username = input("Enter your username: ")
password = input("Enter your password: ")

uname = "whatsup"
cPass = "1212bhututu"
security = "123"

if username == uname:
    if password == cPass:
        print("Login Successful")
    else:
        sCode = input("Enter security code: ")
        if sCode == security:
            print("login Successful")
        else:
            print("Account Locked")
else:
    print("Invalid User")