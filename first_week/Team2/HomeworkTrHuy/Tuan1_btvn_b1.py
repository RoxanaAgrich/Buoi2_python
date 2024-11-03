#Tính tổng các số lẻ (s = 1+3+5+…+n)
#Cách 1 
tong = 0 
a = int(input("Nhap so: ")) #Nhap so n
for sum_odd in range(1, a+1, 2): # Chay tu 1 den n, cách nhau 1 số
        tong += sum_odd # Tính tổng
print("Tong cac so le: ", tong) # Xuất tổng

#Cách 2
result = 0
b = int(input("Nhap so: ")) 
result = range(1, b+1, 2) # Biến lưu giữ giá trị sau khi chạy range
s = sum(result) #Tính tổng 
print("Tong cac so le: ", s) # Xuất tổng