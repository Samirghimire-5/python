# Question 1: Write a Python program that takes the number of electricity units consumed and calculates
# the total bill based on the following rules:
#  If units ≤ 100 → Rate = Rs. 5 per unit
#  If units &gt; 100 and ≤ 200 →
# o First 100 units → Rs. 5 per unit
# o Remaining units → Rs. 8 per unit
#  If units &gt; 200 →
# o First 100 units → Rs. 5 per unit
# o Next 100 units → Rs. 8 per unit
# o Remaining units → Rs. 10 per unit
# If the total bill exceeds Rs. 2000, apply a 10% discount.

eUnits = int(input("Enter your Electricity units consumed: "))
amount = 0
if eUnits <= 100:
    amount = eUnits * 5
elif eUnits > 100 and eUnits <= 200:
    amount = 100 * 5 + (eUnits - 100) * 8
else:
    amount = 100 * 5 + 100 * 8 + (eUnits - 200) * 10

if amount > 2000:
    discount = (amount * 10) / 100
    print("The bill amount is: ", (amount - discount))
else:
    print("The bill amoutn is: ", amount)