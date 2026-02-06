# Question 8: Mobile Recharge Offer System
# Input:
#  Recharge amount
#  User type (New / Existing)
# Rules:
#  New user:
# o ≥ 500 → 25% bonus
# o ≥ 300 → 15% bonus
#  Existing user:
# o ≥ 500 → 15% bonus
# o ≥ 300 → 8% bonus
#  Else → No bonus
# Print total balance after bonus.

rechargeAmt = int(input("Enter Recharge Amount: "))

while True:
    try:
        userType = input("User Type (new / existing)? : ").lower().strip()

        if userType == "new" or userType == "existing":
            break
        else:
            print("please enter correct user type!")
    except:
        print("Invalid input!")


totalBalance = 0


if userType == "new":
    if rechargeAmt >= 500:
        totalBalance = rechargeAmt + (rechargeAmt * 0.25)
    elif rechargeAmt >= 300:
        totalBalance = rechargeAmt + (rechargeAmt * 0.15)
    else:
        totalBalance = rechargeAmt
elif userType == "existing":
    if rechargeAmt >= 500:
        totalBalance = rechargeAmt + (rechargeAmt * 0.15)
    elif rechargeAmt >= 300:
        totalBalance = rechargeAmt + (rechargeAmt * 0.08)
    else:
        totalBalance = rechargeAmt

print("Total Balance after bonus", totalBalance)
