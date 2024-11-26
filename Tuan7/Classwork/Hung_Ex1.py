# Bài 1. Tìm Số Ngẫu Nhiên: Viết một chương trình yêu cầu người dùng nhập một số nguyên 
# dương n, sau đó phát sinh n số ngẫu nhiên và in chúng ra màn hình.
import random
import time
n = int (input("Nhap n: ").strip())
for i in range(n):
    print (random.randint(0,100))
    time.sleep(0.5)
    