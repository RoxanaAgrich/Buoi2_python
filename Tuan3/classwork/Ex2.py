# Bài 2. Viết một chương trình để tạo một lớp trong đó một phương thức chấp nhận một chuỗi 
# từ người dùng và một phương thức để in chuỗi.
# Yêu cầu:
# 1. Tạo một lớp và sử dụng hàm tạo để khởi tạo các giá trị của lớp đó.
# 3. Tạo hai phương thức gọi là get để nhận giá trị của một chuỗi và một phương thức 
# khác gọi là put để in chuỗi đó.
# 4. Tạo đối tượng cho lớp.
# 5. Sử dụng đối tượng, gọi cả hai phương thức.
# 6. In ra chuỗi.
# 7. Thoát

class String:
    def get(self):
        self.str = input("Nhap chuoi: ")
    def put(self):
        print (self.str)

a = String()
a.get()
a.put()