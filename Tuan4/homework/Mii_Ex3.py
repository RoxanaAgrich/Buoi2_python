"""
class: StudentManagement
    -student_list:Student()
    -add()
    - delete()
    -modify()
    -render_Student_List()
class : Student
    - id
    -name
    -render()
"""
class Student():
    def __init__(self,id="S001",name="Дима"):
        self.id = id
        self.name = name
    def enterInfo(self):
        self.id = input("Enter the student id: ")
        self.name = input("Enter the student name: ")
    def render(self):
        print(f"ID :{self.id}")
        print(f"Name :{self.name}")
class StudentManagement():
    students_list=[]
    def add(self):
             n= int(input("Enter the number of student: "))
             for i in range(n):
                 student = Student()
                 student.enterInfo()
                 self.students_list.append(student)
    def delete(self):
        student_id= input("Enter the student id in order to delete: ")
        for i in range(len(self.students_list)):
            if self.students_list[i].id == student_id:
                self.students_list.pop(i)
                break
    def modify_student_Info(self):
        student_id= input("Enter the student id in order to modify: ")
        for i in range(len(self.students_list)):
            if self.students_list[i].id == student_id:
                self.students_list[i].name = input("Enter the new name:  ")
                break
    def render_Students_List(self):
        for i, student in  enumerate(self.students_list,0):
            print("===============================")
            print(f"The student {i+1}: ")
            student.render()
# main function
list = StudentManagement()
list.add()
list.render_Students_List()
list.delete()
list.render_Students_List()
list.modify_student_Info()
list.render_Students_List()




