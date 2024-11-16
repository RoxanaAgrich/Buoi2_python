"""
solves a second degree equation
delta = b**2-4ac
delta>0  the equation has two real solutions
delta ==0 one real solution
delta < 0 No real solution

"""
import math
class Linear_Equation:
    def __init__(self,a=2,b=-4,c=-6):
        self.a=a
        self.b=b
        self.c=c


    def inputInfo(self):
        self.a = float(input("Enter a = "))
        self.b = float(input("Enter b = "))
        self.c = float(input("Enter c = "))
    def solve_linear_equation(self):
        if self.b ==0:
            if self.c ==0:
                return "Infinite solutions"
            else:
                return "No solutions"
        else:
            return -(self.c/self.b)
    def solve_equation(self):

        if self.a ==0:
            if self.b ==0:
                return "No solutions"
            else:
                return f"the linear equation : {self.b}x +{self.c} has solution: x={self.solve_linear_equation()}"
        else:
            delta = self.b**2-4*self.a*self.c
            print(f"{delta}")
            if delta <0:
                return "No solution"
            elif delta ==0:
                x = -self.b/(2*self.a)
                return f"The equation has one solution x= {x}"
            else:
                x1 = (-self.b+math.sqrt(delta))/(2*self.a)
                x2 = (-self.b-math.sqrt(delta))/(2*self.a)
                return f"The equation has two solution x1 = {x1}, x2 = {x2}"
x =  Linear_Equation()
x.inputInfo()
print(f"  {x.solve_equation()}")