#create class:employee 
# Attributes :name, age, address , salary, total working hours
# method: enter the employees' info
#         render those infos
#         calculate the salary
class Employee():
    def __init__(self,name="Mii",age=18,address="Berlin",salary=1000.0, total_working_hours=20.5):
        self.name =name
        self.age = age
        self.address= address
        self.salary= salary
        self.total_working_hours = total_working_hours
#  methods
    # enters the information of employees
    def inputInfo(self):
        self.name =input("enter the employee's name: ")
        self.age = int(input("enter the employee's age: "))
        self.address = input("enter the employee's address: ")
        self.salary = float(input("enter the employee's salary: "))
        self.total_working_hours = float(input("enter the employee's total working hours: "))
    # render the info of employee
    def printInfo(self):
        print(f"the employee's name:{self.name}")
        print(f"the the employee's age:{self.age}")
        print(f"the the employee's address:{self.address}")
        print(f"the the employee's salary:{self.salary}")
        print(f"the the employee's total working hours:{self.total_working_hours}")
        print(f"the the employee's bonus:{self.tinhThuong()}")
    # calculate bonus of employee based on total working hours
    def tinhThuong(self):
        if self.total_working_hours>= 200:
            return self.salary*0.2
        elif self.total_working_hours< 100:
            return 0
        else:
            return self.total_working_hours*0.1
    #Handle multiple employees
    def handleEmployees(self):
        employees_list =[]
        n=int(input("Enter the number of employees: "))
        for i in range(n):
            employee = Employee()
            employee.inputInfo()
            employees_list.append(employee)
        # render info for all employees
        for i, employee in enumerate(employees_list,0):
            print(f"Employee {i} : ")
            employee.printInfo()


employee1 = Employee()
employee1.handleEmployees()






