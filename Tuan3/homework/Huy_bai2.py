import math

class Fraction:
    
    def __init__(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso
        self.rutGon()
        
    def nhap_Fraction(self, tuso, mauso):
        """Nhập giá trị cho phân số"""
        self.tuso = tuso
        self.mauso = mauso
        self.rutGon()
        
    def showFraction(self):
        """Xuất phân số dưới dạng chuỗi"""
        print(f"{self.tuso}/{self.mauso}")
        
    def rutGon(self):
        UCLN = math.gcd(self.tuso, self.mauso)
        self.tuso //= UCLN
        self.mauso //= UCLN

    def daoNguoc(self):
        """Dao phan so"""
        return Fraction(self.mauso, self.tuso)
    
    def congPhanSo(self, otherself):
        """Cong phan so"""
        Phan_Tu = otherself.mauso * self.tuso + self.mauso * otherself.tuso 
        Phan_Mau = self.mauso * otherself.mauso
        return Fraction(Phan_Tu, Phan_Mau)
    
    def truPhanSo(self, otherself):
        """Tru phan so"""
        Phan_Tu =  otherself.mauso * self.tuso - self.mauso * otherself.tuso 
        Phan_Mau = self.mauso * otherself.mauso
        return Fraction(Phan_Tu, Phan_Mau)
    
    def nhanPhanSo(self, otherself):
        """Nhan phan so"""
        Phan_Tu = self.tuso * otherself.tuso
        Phan_Mau = self.mauso * otherself.mauso
        return Fraction(Phan_Tu, Phan_Mau)
    
    def chiaPhanSo(self, otherself):
        """Chia phan so"""
        Phan_Tu = self.tuso * otherself.mauso
        Phan_Mau = self.mauso * otherself.tuso
        return Fraction(Phan_Tu, Phan_Mau)
    
tu1 = int(input("Nhap tu cua phan so thu nhat: "))
mau1 = int(input("Nhap mau cua phan so thu nhat: "))

tu2 = int(input("Nhap tu cua phan so thu hai: "))
mau2 = int(input("Nhap mau cua phan so thu hai: "))

Phanso1 = Fraction(tu1, mau1)
Phanso2 = Fraction(tu2, mau2)

print("Phan so 1: ")
Phanso1.showFraction()
print("Phan so 2: ")
Phanso2.showFraction()

print("\nKet qua cac phep toan: ")

sum_phanso = Phanso1.congPhanSo(Phanso2)
print(f"Phep cong: {tu1}/{mau1} + {tu2}/{mau2} = ", end="")
sum_phanso.showFraction()

sub_phanso = Phanso1.truPhanSo(Phanso2)
print(f"\nPhep tru: {tu1}/{mau1} - {tu2}/{mau2} = ", end="")
sub_phanso.showFraction()

mul_phanso = Phanso1.nhanPhanSo(Phanso2)
print(f"\nPhep nhan: {tu1}/{mau1} x {tu2}/{mau2} = ", end="")
mul_phanso.showFraction()

div_phanso = Phanso1.chiaPhanSo(Phanso2)
print(f"\nPhep chia: {tu1}/{mau1} ∶ {tu2}/{mau2} = ", end="")
div_phanso.showFraction()