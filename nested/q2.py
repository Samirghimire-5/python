# Question 2: Student Scholarship Eligibility
# Write a Python program that takes:
#  Marks in Math, Science, and English
#  Annual family income
# Rules:
# 1. If any subject mark is below 40 → Not eligible
# 2. If all subjects are passed:
# o Calculate average marks
# o If average ≥ 80:
#  If income ≤ 300,000 → Full Scholarship
#  Else → Partial Scholarship
# o If average ≥ 60 and &lt; 80 → Partial Scholarship
# o Else → No Scholarship

math = float(input("Enter your math Marks: "))
science = float(input("Enter your math Science: "))
english = float(input("Enter your math English: "))
annInc = float(input("Enter family anual income: "))

avg = 0

if math < 40 or science < 40 or english < 40:
    print("not Eligible")
else:
    avg = (math + science + english) / 3

if avg >= 80:
    if annInc <= 300000:
        print("Full Scholarship")
    else:
        print("Partial Scholarship")

elif avg >= 60 and avg <= 80:
    print("Partial Scholarship")
else:
    print("No scholarship")