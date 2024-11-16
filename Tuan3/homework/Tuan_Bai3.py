"""Xây dựng lớp số phức có các thuộc tính: phần thực, phần ảo và các phương thức: 
 Cộng, trừ, nhân, chia hai số phức
 Nhập 2 số phức và thực hiện các phép toán trên hai số phức, xuất ra kết quả."""

class SoPhuc:
    def __init__(self, phan_thuc=0, phan_ao=0):
        self.phan_thuc = phan_thuc
        self.phan_ao = phan_ao 

    def __str__(self):  
        # in ra "a + bi"
        return f"{self.phan_thuc} + {self.phan_ao}i" if self.phan_ao >= 0 else f"{self.phan_thuc} - {-self.phan_ao}i" # else phan ao la so am

    def cong(self, other):
        return SoPhuc(self.phan_thuc + other.phan_thuc, self.phan_ao + other.phan_ao)

    def tru(self, other):
        return SoPhuc(self.phan_thuc - other.phan_thuc, self.phan_ao - other.phan_ao)

    def nhan(self, other):
        phan_thuc = self.phan_thuc * other.phan_thuc - self.phan_ao * other.phan_ao
        phan_ao = self.phan_thuc * other.phan_ao + self.phan_ao * other.phan_thuc
        return SoPhuc(phan_thuc, phan_ao)

    def chia(self, other):
        if other.phan_thuc == 0 and other.phan_ao == 0:
            raise ValueError("k the chia cho 0")
        
        mau_so = other.phan_thuc ** 2 + other.phan_ao ** 2
        phan_thuc = (self.phan_thuc * other.phan_thuc + self.phan_ao * other.phan_ao) / mau_so
        phan_ao = (self.phan_ao * other.phan_thuc - self.phan_thuc * other.phan_ao) / mau_so

        # lam tron
        phan_thuc = round(phan_thuc, 3)
        phan_ao = round(phan_ao, 3)

        return SoPhuc(phan_thuc, phan_ao)

def nhap_so_phuc():
    phan_thuc = float(input("nhap pthuc: "))
    phan_ao = float(input("nhap pao: "))
    return SoPhuc(phan_thuc, phan_ao)

print("nhap so phuc t1:")
so_phuc1 = nhap_so_phuc()

print("nhap so phuc t2:")
so_phuc2 = nhap_so_phuc()

tong = so_phuc1.cong(so_phuc2)
hieu = so_phuc1.tru(so_phuc2)
tich = so_phuc1.nhan(so_phuc2)
thuong = so_phuc1.chia(so_phuc2)

print("\nkq:")
print(f"tong: {tong}")
print(f"hieu: {hieu}")
print(f"tich: {tich}")
print(f"thuong: {thuong}")
