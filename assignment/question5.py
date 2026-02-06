# Question 5: Hospital Billing System
# Write a Python program that takes:
#  Patient type (General / Emergency / VIP)
#  Number of days admitted
#  Medicine cost
# Rules:
#  General: Rs. 1500 per day
#  Emergency: Rs. 2500 per day
#  VIP: Rs. 4000 per day
#  If total bill > 20,000 → 10% discount
#  If total bill > 50,000 → 20% discount
# Print final bill.

type = input("Enter Patient type (General / Emergency / VIP): ").lower().strip()
daysAdmitted = int(input("Enter admitted days: "))
medCost = float(input("Enter medicine cost of the patient: "))

bill = 0
generalRate = 1500
emergencyRate = 2500
vip = 4000

if type == "general":
    bill = generalRate * daysAdmitted
elif type == "emergency":
    bill = emergencyRate * daysAdmitted
elif type == "vip":
    bill = vip * daysAdmitted

discount = 0
if bill > 20000:
    discount = (20000 * 10) / 100
elif bill > 50000:
    discount = (50000 * 20) / 100

totalBill = bill - discount
print("The total bill is : ", totalBill)
