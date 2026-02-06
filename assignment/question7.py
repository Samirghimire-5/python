# Question 7: Smart Parking Fee System
#
# Input:
#  Vehicle type (Bike / Car / Truck)
#  Hours parked
# Rates:
#  Bike → Rs. 20/hr
#  Car → Rs. 50/hr
#  Truck → Rs. 100/hr
# Rules:
#  If hours > 5 → 10% discount
#  If hours > 10 → 20% discount
#  If vehicle type invalid → Error message

vehicleType = input("Enter vehicle type (Bike / Car / Truck): ").lower().strip()

while True:
    try:
        parkedHour = int(input("Enter parked hours: "))
        if parkedHour > 0:
            break
        else:
            print("Hours must be positive!")
        # this catches values like 10.10, "samir" (only integers are allowed any other type will throw error)
    except ValueError:
        print("Please enter a valid whole number!")


def feeCalculator(parkingRate, parkedHour):
    totalFee = parkingRate * parkedHour

    if parkedHour > 10:
        totalFee = totalFee * 0.80  # 20% discount (pay 80%)
    elif parkedHour > 5:
        totalFee = totalFee * 0.90  # 10% discount (pay 90%)

    return totalFee


# rates per hour
bike = 20
car = 50
truck = 100

if vehicleType == "bike":
    fee = feeCalculator(bike, parkedHour)
    print(f"Total fee: Rs. {fee}")
elif vehicleType == "car":
    fee = feeCalculator(car, parkedHour)
    print(f"Total fee: Rs. {fee}")
elif vehicleType == "truck":
    fee = feeCalculator(truck, parkedHour)
    print(f"Total fee: Rs. {fee}")
else:
    print("Invalid vehicle type")
