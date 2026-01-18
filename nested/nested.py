math = float(input("Enter your math Marks: "))
science = float(input("Enter your science Marks: "))
english = float(input("Enter your english Marks: "))

if math < 35 or english < 35 or science < 35:
    print("You are fail repet the semester")
else:
    average = (math + science + english) / 3
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
    print("Math has highest score: ", math)
elif science > math and science > english:
    print("Science has highest score: ", science)
elif english > math and english > science:
    print("English has highest score: ", english)
else:
    print("Two or more subjects have the same highest marks")
