"""
class Student: id, gpa, age, class
method : inputInfo()
         showInfo()
         checkScholarship()
"""
# builds class Student
class Student():
    def __init__(self,id="0123456789",gpa=10,age=18,class_name="14DHTH05"):
        self.id=id
        self.gpa=gpa
        self.age = age
        self.class_name =class_name
    def inputInfo(self):
        while True:
            self.id= input("Enter student ID(10 characters): ")
            if len(self.id)==10:
                break
            print("Student Id must be 10 characters long ")
        while True:
            self.gpa = float(input("Enter the student gpa:(from 0 to 10) "))
            if self.gpa >=0 and self.gpa<=10:
                break
            print("GPA must be between 0 and 10")
        while True:
            self.age= int(input("Enter the age (>=18)"))
            if self.age >=18:
                break
            print("Age must be 18 or older")
        while True:
            self.class_name= input("enter the class name (ex: 12DHHT02)")
            if self.validClassName(self.class_name):
                break
            print("The class name is invalid ")
# render the info of employee
    def printInfo(self):
        print(f"the student's id:{self.id}")
        print(f"the the student's gpa:{self.gpa}")
        print(f"the the student's age:{self.age}")
        print(f"the the student's class :{self.class_name}")
        print(f"the student is eligible for a scholarship :{self.checkScholarship()}")
#check if the student is eligible for a scholarship
    def checkScholarship(self):
        return "Yes" if self.gpa>=8 else "No"
    @staticmethod
    def validClassName(class_name):
        if(
                len(class_name) >= 8
                and class_name.startswith("12")
                and class_name[2:4] == "DH"
                and (class_name[4:6]=="HT" or class_name[4:7]=="MMT" )
                and class_name[-2:].isdigit()
                and 1 <= int(class_name[-2:]) <= 99
        ):
            return True
        return False

    def handleStudents(self):
        students_list = []
        n = int(input("Enter the number of employees: "))
        for i in range(n):
            print(f"Enter the student's information {i+1}")
            student = Student()
            student.inputInfo()
            students_list.append(student)
        # render info for all employees
        for i, student in enumerate(students_list,0):
            print(f"Student {i+1}: ")
            student.printInfo()

student_list = Student()
student_list.handleStudents()


