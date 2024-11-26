# Bài 3. Tính Toán Trung Bình: Viết một chương trình tính toán trung bình của một dãy số
# nguyên ngẫu nhiên từ 1 đến 100.
import random
l= [random.randint(1,100) for i in range(random.randint(1,100))]
print(l)
print(sum(l)/len(l))