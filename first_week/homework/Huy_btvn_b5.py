# Nhập số nguyên n. Viết chương trình để tạo ra một dãy số chứa (i : i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dãy số này. 
# Ví dụ: số n là 8 thì đầu ra sẽ là: 1: 1 2: 4 3: 9 4: 16 5: 25 6: 36 7: 49 8: 64
import math
#Cách 1
a = int(input("Nhap n: "))
d = dict() #Dict dùng để lưu trữ các giá trị mà ko có quy tắc bất kì
for A in range(1, a+1,1): # Chạy điều kiện
    d[A] = A*A #Chạy A thông qua "d" đã lưu trữ
print(d)

#Cách 2
b = int(input("Nhap n: "))
for C in range(1, b+1,1):
    print("%d: %d" % (C, C * C), end= " | ")
