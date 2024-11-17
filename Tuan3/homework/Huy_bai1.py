from datetime import datetime

class Person:
    def __init__(self, Name, Country, Date_of_birth): 
        self.Name = Name
        self.Country = Country
        self.Date_of_birth = datetime.strptime(Date_of_birth, "%d/%m/%Y")
    
    def calculateAge(self):
        today = datetime.today()
        age = today.year - self.Date_of_birth.year - ((today.month, today.day) < (self.Date_of_birth.month, self.Date_of_birth.day))
        return age
          
    def showInfo(self):
        age = self.calculateAge()
        print("Name: ", self.Name)
        print("Country: ", self.Country)
        print("Date of birth: ", self.Date_of_birth.strftime("%d/%m/%Y"))
        print(f"Tuoi: {age}")
        
person = Person("Tran Van A", "VietNam", "11/03/2000")
person.showInfo()


   
    
    
