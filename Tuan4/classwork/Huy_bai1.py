"""Tạo ba lớp, Person có 2 thuộc tính: name, age, Employee (Nhân viên) có 2 thuộc tính: emp_id, salary và Student (Sinh viên) có 2 thuộc tính: student_id , grade
Sử dụng nhiều kế thừa để tạo một lớp “PersonInfo” kế thừa từ cả “Nhân viên” và “Sinh viên”.
Thêm các thuộc tính và phương thức cụ thể cho từng lớp.
Ví dụ: PersonInfo("John", 30, "E123", 50000, "S456", "A")
Kết quả:
Name: John
Age: 30
Employee ID: E123
Salary: 50000
Student ID: S456
Grade: A"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age) 
        self.emp_id = emp_id
        self.salary = salary

class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade
        
class PersonInfo(Employee, Student):
    def __init__(self, name, age, emp_id, salary, student_id, grade):
        Employee.__init__(self, name, age, emp_id, salary)
        Student.__init__(self, name, age, student_id, grade)
        
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")
        
person = PersonInfo("John", 30, "E123", 50000, "S456", "A")
person.show_info()
