# Bài 2. Sắp Xếp Dãy Số Ngẫu Nhiên: Viết một chương trình phát sinh một dãy số ngẫu nhiên, 
# sau đó sắp xếp dãy số đó theo thứ tự tăng dần và in ra màn hình.

import random
import time
n = int (input("Nhap n: ").strip())
l = [random.randint(0,100) for i in range(n)]
for i in l:
    print (i,end =" ")
l.sort()
print()
print (l)
