"""
class: Circle
    radius:float
    calculate_perimeter()
    calculate_area()
"""
import math


class Circle :
    def __init__(self, radius=9):
        self.radius =radius
    def calculate_perimeter(self):
        return 2*math.pi*self.radius
    def calculate_area(self):
        return math.pi*(self.radius**2)
    def inputInfo(self):
        self.radius= float(input("Enter the radius of circle: "))
    def display(self):
        print(f"The circle with radius {self.radius} ")
        print(f"The area {self.calculate_area()} ")
        print(f"The perimeter{self.calculate_perimeter()} ")
circle = Circle()
circle.inputInfo()
circle.display()