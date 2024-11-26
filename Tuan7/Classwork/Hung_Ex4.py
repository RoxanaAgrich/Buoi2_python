# Bài 4. Tìm Số Lớn Nhất và Nhỏ Nhất: Viết một chương trình tạo một dãy số ngẫu nhiên, sau 
# đó tìm và in ra số lớn nhất và nhỏ nhất trong dãy số đó.
import random
l= [random.randint(1,100) for i in range(random.randint(1,100))]
print(l)
print(max(l))
print(min(l))