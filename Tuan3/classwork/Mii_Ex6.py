"""
class: Triangle
triangle's sides : a,b,c
method: enter the info
        is that triangle valid
        render
        calculate the perimeter
        calculate the area
        determine the type of triangle
"""
import math
class Triangle():
    def __init__(self,a=3,b=4,c=5):
        self.a =a
        self.b =b
        self.c =c
    # enters the sides of triangle
    def inputInfo(self):
        while True:
            a= float(input("Enter the triangle's side a: "))
            b= float(input("Enter the triangle's side b: "))
            c= float(input("Enter the triangle's side c: "))
            if not self.is_valid_triangle(self.a,self.b,self.c):
                break
            print("The sides entered do not form a valid triangle. Please try again")
    # is that triangle valid
    @staticmethod
    def is_valid_triangle(a,b,c):
        return True if a+b>c and a+c>b and b+c>a else False
    # determines the triangle type
    def triangle_Type(self):
        if not self.is_valid_triangle(self.a,self.b, self.c ):
            return "The sides entered do not form a valid triangle"

        if self.a == self.b == self.c :
            return "Equilateral triangle"
        elif self.a == self.b or self.a == self.c or self.c == self.b:
            return "Isosceles triangle"
        elif (self.a**2+self.b**2 == self.c**2
            or self.a**2+self.c**2 == self.b**2
            or self.b**2+self.c**2 == self.a**2
        ):
            return "Right triangle"
        else:
            return"Normal triangle"

    # calculates the perimeter
    def calculate_perimeter(self):
        if not self.is_valid_triangle(self.a, self.b, self.c):
            return "Cannot calculate perimeter: Invalid triangle"
        return self.a+self.b+self.c
    # calculates the area
    def calculate_area(self):
        if not self.is_valid_triangle(self.a, self.b, self.c):
            return "Cannot calculate area: Invalid triangle"
        s = self.calculate_perimeter()
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

# render the triangle
    def render(self):
        print(f"This is {self.triangle_Type()} with 3 side a={self.a}, b={self.b}, c={self.c} ")
        print(f" perimeter is: {self.calculate_perimeter()}")
        print(f" area is: {self.calculate_area()}")
equilateral_triangle = Triangle(3,3,3)
equilateral_triangle.render()
isosceles_triangle = Triangle(4,4,6)
isosceles_triangle.render()
invalid_triangle = Triangle(1,3,2)
invalid_triangle.render()




