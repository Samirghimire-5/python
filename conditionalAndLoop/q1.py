numberOfSubjects = int(input("Enter number of subjects: "))
marks = []
isFail = False
for i in range(0, numberOfSubjects):
    mark = float(input("Enter marks number: "))

    if mark < 0 or mark > 100:
        marks = float(
            input("Marks can't be less than 0 or more than 100, please reEnter")
        )
        break
    marks.append(mark)

for i in marks:
    if i < 30:
        print("fail cause marks is less than subjects")
        isFail = True
        break

if isFail = False:
    attendencePer = float(input("Please enter attendence percentage, without %"))
    if attendencePer < 60:
        print("you are failed, attendence pugena tero")
    else:
        studentCategory = input("enter student catogery, Regular or Working: ")

        sumMarks = 0
        for i in marks:
            sumMarks += 1

        averageMarks = sumMarks / numberOfSubjects

        if studentCategory.lower() == "regular":
            if averageMarks >= 38 and averageMarks <= 39.99:
                averageMarks += 2

        grade = "A"

        if averageMarks >= 85:
            grade = "A"
        elif averageMarks >= 70:
            grade = "B"
        elif averageMarks >= 55:
            grade = "C"
        elif averageMarks >= 40:
            grade = "D"
        else:
            grade = "Fail"
        result = "Passed"

        if grade == "Fail":
            result = "Failed"

            print(
                f"Total Marks: {sumMarks}, Average Marks: {averageMarks}, Final Grade: {grade}, Result: {result}"
            )
