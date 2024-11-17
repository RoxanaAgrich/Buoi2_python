"""Tính chu vi & diệntích các hình (abstract)
Viết chương trình tính chu vi và điện tích của một số hình như sau:
 Hình tròn
 Hình chữ nhật
 Hình tam giác"""

from abc import ABC, abstractmethod
import math

class Hinh(ABC):

    def chuvi(self):
        pass
    
    def dientich(self):
        pass
    
class Htron(Hinh):
    def __init__(self, bkinh):
        self.bkinh = bkinh
        
    def chuvi(self):
        return 2 * math.pi * self.bkinh
    
    def dtich(self):
        return math.pi * (self.bkinh ** 2)
    
class Hcn(Hinh):
    def __init__(self, cdai, crong):
        self.cdai = cdai
        self.crong = crong
        
    def chuvi(self):
        return 2 * (self.cdai + self.crong)
    
    def dtich(self):
        return self.cdai * self.crong
    
class Htg(Hinh):
    def __init__(self, canha, canhb, canhc):
        self.canha = canha
        self.canhb = canhb
        self.canhc = canhc
        
    def chuvi(self):
        return self.canha + self.canhb + self.canhc
    
    def dtich(self):
        p = self.chuvi() / 2
        return math.sqrt(p * (p - self.canha) * (p - self.canhb) * (p - self.canhc))
    
circle = Htron(6)  # Bán kính 6
print("Chu vi cua hinh tron: ", circle.chuvi())
print("Dien tich cua hinh tron: ", circle.dtich())

rectangle = Hcn(4, 8)  # Chiều dài 4, chiều rộng 8
print("Chu vi cua hinh chu nhat: ", rectangle.chuvi())
print("Dien tich cua hinh chu nhat: ", rectangle.dtich())

triangle = Htg(3, 4, 5)  # Ba cạnh 3, 4, 5
print("Chu vi cua hinh tam giac: ", triangle.chuvi())
print("Dien tich cua hinh tam giac: ", triangle.dtich())