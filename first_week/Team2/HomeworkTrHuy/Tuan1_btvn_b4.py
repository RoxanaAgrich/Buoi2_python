#Tính n! (n giai thừa)
import math
#Cách 1 
tong = 1
a = int(input("Nhap so: ")) #Nhap so n
for sum_odd in range(1, a+1, 1): # Chay tu 1 đến n, cách nhau 1 số
        tong *= sum_odd # Tính tổng nhân các số chẵn
print("Nhan cac so chan: ", tong) # Xuất tổng

#Cách 2
result = 1
b = int(input("Nhap so: ")) 
result = range(1, b+1, 1) # Biến lưu giữ giá trị sau khi chạy range
s = math.prod(result) # Tính tổng nhân các số chẵn
print("Nhan cac so chan: ", tong) # Xuất tổng
