# input : điểm sinh viên  trên thang điểm 10
# output : cho biết sinh viên đó đặt hay không đặt theo
# thang điểm 4 thuốc điểm nào
student_score = float(input('Enter the score: '))

while student_score < 0 or student_score > 10:
    print("The score is invalid. Please enter a valid score.")
    student_score = float(input("Enter the score: "))

if student_score <= 3.9:
    grade = "F"
    score = 0
elif student_score <= 5.4:
    grade = "D"
    score = 1
elif student_score <= 6.9:
    grade = "C"
    score = 2
elif student_score <= 8.4:
    grade = "B"
    score = 3
else:
    grade = "A"
    score = 4

if grade == "F":
    print(f"The student with score {student_score} has failed. Grade: {grade} = {score}")
else:
    print(f"The student with score {student_score} achieved Grade: {grade} = {score}")