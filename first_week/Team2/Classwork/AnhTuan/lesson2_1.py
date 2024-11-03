''' Viết hàm tạo mảng số nguyên a với n phần tử và mảng b chỉ chứa các phần tử chẵn của a.'''

import random

def tao_mang_a(n, min_val=1, max_val=100):
    # Tao random a
    a = [random.randint(min_val, max_val) for _ in range(n)]
    return a

def tao_mang_b(a):
    # Tao b la tap hop con cua a
    b = [x for x in a if x % 2 == 0]
    return b

n = int(input("Nhap so pt mang a: "))
a = tao_mang_a(n)
b = tao_mang_b(a)

print("Mang a:", a)
print("Mang b (pt chan):", b)

