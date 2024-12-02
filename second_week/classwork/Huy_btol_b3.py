# Cho mảng 2 chiều a có m dòng, n cột chứa số nguyên
#Arr là chạy dòng
#Arr[i] là chạy cột
import random
import math
#Tạo mảng rỗng
Arr = []
Sum_rows = []
Prods = []
def cau_a():
    #Nhập n hàng và m cột
    n = int(input("Nhap so hang: "))
    m = int(input("Nhap so cot: "))

    for i in range(n):
        Arr.append([]) # Thêm số lượng dòng trong list arr
        for j in range(m): 
            x = random.randint(1,100) # Nhập giá trị cho từng cột ở từng dòng
        #Thêm phần tử vào hàng i
            Arr[i].append(x)
    for row in Arr:
        print(row)
        
def cau_b():
    #Xuất các phần tử thuộc dòng k
    dk = int(input("Chọn dòng k để xuất các phần tử: "))
    if 0 <= dk <= len(Arr):
        print("Các phần tử thuộc dòng %d: " % dk, Arr[dk])
    else:
        print("Dòng không hợp lệ!")
def cau_c():
    #Xuất các phần tử thuộc cột k
    dk = int(input("Chọn cột k để xuất các phần tử: "))
    if 0 <= dk <= len(Arr):
        Colum = [row[dk] for row in Arr] # Lấy vị trí thứ "dk" ở mỗi dòng 
        print("Các phần tử thuộc cột %d: " % dk, Colum)
    else:
        print("Dòng không hợp lệ!")
        
def cau_d():
    #Tìm dòng có tổng lớn nhất
    for row in Arr:
        Sum_row = sum(row) #Tính tổng tất cả hàng ngang
        Sum_rows.append(Sum_row) #Thêm phần tử vào cuối List Sum_rows từ Sum_row
    
    max_row = max(Sum_rows) #Tìm dòng lớn nhất
    max_GT = Sum_rows.index(max_row)  #Đưa ra thứ tự hàng của hàng có giá trị lớn nhất
    
    print(f"Dòng {max_GT} có tổng lớn nhất: {max_row}")
    print("Dòng %d: " % max_GT, Arr[max_GT])
    
def cau_e():
    #Tìm cột có tích nhỏ nhất
    num_cols = len(Arr[0])

    for Col in range(num_cols): 
        Prod = math.prod(row[Col] for row in Arr)
        Prods.append(Prod) #Thêm phần tử vào cuối list Prods từ Prod

    min_prod = min(Prods) # Tìm cột nhỏ nhất
    min_Tich = Prods.index(min_prod)  #Đưa thứ tự cột của cột có giá trị nhỏ nhất
    
    print(f"Cột {min_Tich} có tích nhỏ nhất: {min_prod}")
    print("cột %d: " % min_Tich, [row[min_Tich] for row in Arr])

def cau_f():
    #Xuất các phần tử thuộc dòng chẵn và cột lẻ trong mảng
    for i in range(0,(len(Arr)), 2): #Chạy dòng
        if i % 2 == 0: 
            for j in range(1,(len(Arr[i])), 2): #Chạy cột của từng dòng
                if j % 2 != 0:
                    print(f"Phần tử tại [{i}] [{j}]: {Arr[i][j]}")
                    
def cau_g():
    #Tính trung bình cộng các phần tử chẵn thuộc dòng lẻ trong mảng
    total = 0
    count = 0
    
    for i in range(1, len(Arr), 2): #Chạy dòng chẵn
        for GT in Arr[i]: # Chạy các giá trị trong cột 
            if GT % 2 == 0:
                total += GT
                count += 1
    if count == 0:
        print("Không có giá trị nào!")
    else:
        avg = total / count
        print(f"Trung bình cộng các phần tử chẵn ở dòng lẻ: {avg}")

def cau_h():
    #Tính trung bình cộng các phần tử thuộc biên
    count = 0
    total = 0
    #Tính tổng ở dòng đầu
    for i in range(len(Arr[0])):
            total += Arr[0][i]
            count += 1
    #Tính tổng ở dòng cuối
    for j in range(len(Arr[-1])):
            total += Arr[-1][j]
            count += 1
    #Tính tổng ở các cột
    for k in range(1, len(Arr) -1):
        #Tính tổng ở cột đầu
            total += Arr[k][0]
            count += 1
        #Tính tổng ở cột cuối
            total += Arr[k][-1]
            count += 1
    avg = total / count
     
    print(f"Trung bình cộng các phần tử ở biên: {avg}")

def cau_i():
    #Tính trung bình tích các phần tử không thuộc biên
    count = 0
    total = 1
    #Tính tích
    for i in range(1, len(Arr) - 1): #Bỏ qua dòng đầu và cuối
        for j in range(1, len(Arr[i]) - 1): #Bỏ qua cột đầu và cuối
            total *= Arr[i][j] 
            count += 1
    avg = total / count
    print(f"Trung bình tích các phần tử không thuộc biên: {avg}")
        
def exit():
    return "Thoat chuong trinh !"


menu = {0: exit, 1: cau_a,2: cau_b , 3: cau_c, 4: cau_d, 5: cau_e , 6: cau_f, 7: cau_g , 8: cau_h , 9: cau_i,}

while True:
    print("\nChọn chức năng: ")
    print("1. Tạo ma trận.")
    print("2. Xuất các phần tử thuộc dòng k.")
    print("3. Xuất các phần tử thuộc cột k.")
    print("4. Tìm dòng có tổng lớn nhất.")
    print("5. Tìm cột có tích nhỏ nhất.")
    print("6. Xuất các phần tử thuộc dòng chẵn và cột lẻ trong a.")
    print("7. Tính trung bình cộng các phần tử chẵn thuộc dòng lẻ của a")
    print("8. Tính trung bình cộng các phần tử thuộc biên.")
    print("9. Tính trung bình tích các phần tử không thuộc biên. ")
    print("0. Thoát chương trình")


    nhap = int(input("Chọn chức năng: "))
    
    
    if nhap == 0:
        menu[0]()
        break
    
    #lambda: hàm ẩn danh
    result = menu.get(nhap, lambda: print("Chức năng không hợp lệ. Vui lòng chọn lại."))

    result()
