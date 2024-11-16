"""
solves a first degree equation
 ax+b=0=>  x= -b/a
"""

class Linear_Equation:
    def __init__(self,a=2,b=4):
        self.a=a
        self.b=b

    def inputInfo(self):
        self.a = float(input("Enter a = "))
        self.b = float(input("Enter b = "))

    def solve_linear_equation(self):
        if self.a ==0:
            if self.b ==0:
                return "Infinite solutions"
            else:
                return "No solutions"
        else:
            return -(self.b/self.a)
    def display(self):
        print(f"the linear equation : {self.a}x +{self.b} has solution: x={self.solve_linear_equation()}")
x =  Linear_Equation()
x.inputInfo()
x.display()