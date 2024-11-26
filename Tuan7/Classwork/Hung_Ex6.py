# Bài 6. Chọn Số Ngẫu Nhiên từ Danh Sách: Viết một chương trình cho phép người dùng nhập 
# một danh sách các số nguyên, sau đó chọn ngẫu nhiên một số từ danh sách đó và in ra màn 
# hình.
import random
choice = input("Nhap list: ").strip(" ").split()
choice = [int(i) for i in choice]
print(random.choice(choice))