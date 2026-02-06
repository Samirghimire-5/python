# Question 9: Online Exam Login System
# Input:
#  Username
#  Password
#  OTP
# Rules:
#  If username incorrect → Access Denied
#  If password incorrect → Try OTP
#
#  If OTP correct → Login successful
#  If OTP wrong → Account blocked
#  After 3 failed attempts → Permanently locked


# temp storage
correct_username = "student123"
correct_password = "pass123"
correct_otp = "123456"

failed_attempts = 0

while failed_attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    # check username
    if username != correct_username:
        print("Access Denied - Username incorrect")
        failed_attempts += 1
        if failed_attempts >= 3:
            print("Account permanently locked")
            break
        continue

    # check password
    if password != correct_password:
        print("Password incorrect - Try OTP")
        otp = input("Enter OTP: ")

        if otp == correct_otp:
            print("Login successful!")
            failed_attempts = 0  # reset attempts on success
            break
        else:
            print("OTP wrong - Account blocked")
            failed_attempts += 1
            if failed_attempts >= 3:
                print("Account permanently locked")
            break

    # password correct login successful
    print("Login successful!")
    failed_attempts = 0  # reset on success
    break
