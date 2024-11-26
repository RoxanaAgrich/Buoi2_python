# Câu 2. Xây dựng một lớp Sách (Book) có các thuộc tính: name, author, date.
#  Xây dựng file input.json bao gồm mảng thông tin của nhiều quyển sách.
#  Đọc file thành một list các đối tượng Book.
#  Xây dựng các chức năng CRUD: Thêm một quyển sách mới, Truy vấn danh sách 
# sách theo tác giả, Chỉnh sửa thông tin sách (Cho người dùng chọn từ danh sách quyển sách 
# cần sửa) và Xóa một quyển sách (Cho người dùng chọn từ danh sách quyển sách cần xóa).
#  Xây dựng chức năng lưu thông tin lại file json.
#  Xử lý lỗi khi cần thiết
import copy 
import os
import json
import time
class BookManager:
    def __init__(self,l):
        self.List = copy.deepcopy(l)
    def Dlt(self,Name):
        for i in self.List:
            if i["name"].casefold() == Name.casefold():
                self.List.remove(i)
                print("Done!!")
                break
        else:
            print("Khong ton tai.")
    def Add(self):
        a = input("Nhap thong tin (Ten_Tacgia_Nam): ").split("_")
        key = ["name","author","date"]
        dic = dict(zip(key,a))
        self.List.append(dic)
        print("Done!")
    def Show(self):
        for i in self.List:
            print(f"Tên sách: {i['name']:<20} Tác giả: {i['author']:<16} Thời gian: {i['date']}")


try:
    path = os.getcwd() + r"\Tuan6\Data\homework\dataEx2.json"
    with open(path, "r", encoding = "utf-8") as file:
        data = json.load(file)
        listbook = BookManager(data)
        listbook.Show()
        time.sleep(4)
        os.system("cls")
        listbook.Add()
        listbook.Show()
        time.sleep(4)
        os.system("cls")
        s = input("Nhap ten cuon sach can xoa: ").strip()
        listbook.Dlt(s)
        listbook.Show()
        time.sleep(4)
        
except FileNotFoundError:
    print ("Khong tim thay file!")
    
try:
    path = os.getcwd() + r"\Tuan6\output\homework\Ex2.json"
    with open(path, "w", encoding = "utf-8") as file:
        json.dump(listbook.List, file,ensure_ascii=False, indent=4)
        
except FileNotFoundError:
    print ("Khong tim thay file!")