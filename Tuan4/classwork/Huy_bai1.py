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
