#Tính tích các số chẵn (tich = 2x4x6x…x n)
import math
#Cách 1 
tong = 1
a = int(input("Nhap so: ")) #Nhap so n
for sum_odd in range(2, a+1, 2): # Chay tu 2 den n, cách nhau 1 số
        tong *= sum_odd # Tính tổng nhân các số chẵn
print("Nhan cac so chan: ", tong) # Xuất tổng

#Cách 2
result = 1
b = int(input("Nhap so: ")) 
result = range(2, b+1, 2) # Biến lưu giữ giá trị sau khi chạy range
s = math.prod(result) # Tính tổng nhân các số chẵn
print("Nhan cac so chan: ", tong) # Xuất tổng
