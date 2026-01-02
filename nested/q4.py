# Question 4: Traffic Fine System
# Write a Python program that accepts:
#  Vehicle speed
#  Whether the driver has a valid license (yes or no)
# Rules:
# 1. If speed ≤ 60 → No fine
# 2. If speed &gt; 60:
# o If speed ≤ 90:
#  If license is valid → Fine Rs. 500
#  Else → Fine Rs. 1000
# o If speed &gt; 90:
#  If license is valid → Fine Rs. 2000
#  Else → License Cancelled + Fine Rs. 3000


speed = float(input("Enter Vehicle Speed: "))
license = input("Does Driver has a valid License: ")
isLicValid = license.strip().lower()
fine = 0
isLicCanclled = False

if speed <= 60:
    print("No Fine")
if speed > 60:
    if speed <= 90:
        if isLicValid == "yes":
            fine = 500
        else:
            fine = 1000
    else:
        if isLicValid == "yes":
            fine = 2000
        else:
            fine = 3000
            isLicCanclled = True

if isLicCanclled:
    print("Fine: ", fine, ", license Canclled")
else:
    print("Fine: ", fine)
