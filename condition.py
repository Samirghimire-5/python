# write a program to see wheather a given num is even or odd.
num = int(input("give a number: "))

if (num % 2 == 0): 
    print("The number is even")
else:
    print("The number is odd")


# write a program to check wheather a number pos, neg or zero.
num = int(input("give a number: "))

if (num > 0):
    print("The num is positive")
elif (num < 0):
    print("The num is Negative")
else:
    print("The num is zero")



# write a program to check wheather a character is vowel or consonent
vowelArr = ["a", "e" "i", "o", "u"]
char = input("give a character: ").lower()

if (len(char) > 1):
    print("The char length shouldn't be more than 1")
elif (char in vowelArr):
    print("The char is vowel")
else:
    print("The char is consonent")


# write a program to find the largest of three numbers using conditional statements.
# write a program to take two numbers and and operator (+, -, *, /) and perform operations using if elif else
# write a program to calculate electrical bill first 100 unit 5rs per unit, next 100 unit 7 rs per unit,
    # above 200 unit 10 rs per unit, apply 5% discount if the bill is greater than 2000 rs.
# write a program to check wheather a triangle is equalator, isosolis , scalent triangel or invalid.
# write a program to simulate atm withdrawl.
    # check if balance is sufficient,
    # check if amt is multiple of 100,
    # deduct amount and display remaining balance
