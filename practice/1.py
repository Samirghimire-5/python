# 25. Write a Python program, algorithm, flowchart that accepts three subject marks from the user: Math, Science, and English. Using nested if-else statements, determine and display the student's final grade based on the following rules:
# Rules:
# 1. If any subject is below 35, the student fails.
# 2. If the student passes all subjects, calculate the average:
# average (Math+Science+English)/3
# 3. Based on the average:
# 90 and above → Grade A+
# 80-89 Grade A
# 70-79 Grade B
# 60-69 Grade C
# 50-59 Grade D
# Below 50→→ Grade E
# 4. If two or more subjects have the same highest marks, display a message saying:
# "Two or more subjects share the highest score."
# Otherwise, display the subject with the highest marks.


math = int(input("math: "))
english = int(input("english: "))
science = int(input("science: "))

if math < 35 or science < 35 or english< 35:
  print("fail")
else:
  average = math + science + english / 3

  if average >= 90: 
    print("Grade A+")
  elif average >= 80: 
    print("Grade A")
  elif average >= 70: 
    print("Grade B")
  elif average >= 60: 
    print("Grade C")
  elif average >= 50: 
    print("Grade D")
  else:
    print("Grade E")

if math > science and math > english: 
  print("Math is greater", math)
elif science > math and science > english: 
  print("science is greater", science)
elif english > science and english > math: 
  print("english is greater", english)
else: 
  print("Two or more subjects share the highest score.")