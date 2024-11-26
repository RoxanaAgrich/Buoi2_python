# Bài 5. Xoá Phần Tử Trùng Lặp: Viết một chương trình tạo một danh sách ngẫu nhiên gồm 
# các phần tử có thể trùng lặp, sau đó xoá các phần tử trùng lặp và in ra danh sách
# sau khi đã xoá.
import random
l= [random.randint(1,100) for i in range(random.randint(1,100))]
print(l)
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)

print(l1)