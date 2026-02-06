# Question 6: Exam Result Processing System
# Input:
#  Marks in 5 subjects
# Rules:
#  If any subject < 35 → Fail
#  If passed:
# o Average ≥ 85 → Distinction
# o Average ≥ 70 → First Division
# o Average ≥ 50 → Second Division
# o Else → Third Division
#  If all subjects ≥ 90 → Scholarship Eligible

m1 = float(input("Enter 1st subject mark: "))
m2 = float(input("Enter 2st subject mark: "))
m3 = float(input("Enter 3st subject mark: "))
m4 = float(input("Enter 4st subject mark: "))
m5 = float(input("Enter 5st subject mark: "))

if m1 < 35 or m2 < 35 or m3 < 3 or m4 < 35 or m5 < 35:
    print("Fail Vayo hai")
else:
    average = (m1 + m2 + m3 + m4 + m5) / 5

    if average >= 85:
        print("Distinction")
    elif average >= 70:
        print("First Division")
    elif average >= 50:
        print("First Division")
    else:
        print("Third Division")

if m1 >= 90 or m2 >= 90 or m3 >= 90 or m4 >= 90 or m5 >= 90:
    print("Scholarship Eligible")
