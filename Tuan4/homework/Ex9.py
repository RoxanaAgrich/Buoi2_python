# Bài 9. Một sinh viên gồm các thông tin sau: 
#  Mã sinh viên là chuỗi có 10 ký tự
#  Tên là chuỗi tối đa 20 ký tự
#  Năm sinh là một số nguyên 
#  Điểm trung bình là một số thực a. 
# (1) Xây dựng cấu trúc SINHVIEN mô tả một sinh viên 
# (2) Cho một mảng có n sinh viên. 
# (3) Viết hàm cho biết có bao sinh viên đủ điều kiện lên lớp, biết rằng sinh viên đủ điều 
# kiện lên lớp khi điểm trung bình lớn hơn hoặc bằng 5. 
# (4) Xuất các sinh viên đủ 20 tuổi. 
# (5) Đếm số sinh viên học hệ đại học, biết rằng sinh viên hệ DH có mã sinh viên chứa 2 ký 
# tự DH ở vị trí 2,3 trong chuỗi. VD: 02DH0001. 
# (6) Cho biết trong mảng có bao nhiêu sinh viên có tên «Lan» 
# (7) Cho biết trong mảng có bao nhiêu sinh viên có họ «Phan

from datetime import datetime

class SinhVien:
    def __init__(self, masv, ten, namsinh, tb):
        self.Ma = masv
        self.Ten = ten
        self.NamSinh = namsinh
        self.TrungBinh = tb

    def is_qualified(self):
        return self.TrungBinh >= 5

    def is20(self):
        current = datetime.now().year
        return current - self.NamSinh >= 20

    def isDH(self):
        return self.Ma[2:4] == "DH"


class SinhVienManager:
    def __init__(self):
        self.dsSV = []

    def Add_std(self, masv, ten, namsinh, tb):
        sinh_vien = SinhVien(masv, ten, namsinh, tb)
        self.dsSV.append(sinh_vien)

    def svdudieukien(self):
        return sum(sv.is_qualified() for sv in self.dsSV)

    def xuatSv20(self):
        sv = [sv for sv in self.dsSV if sv.is20()]
        return sv

    def dem_sv_dh(self):
        return sum(sv.isDH() for sv in self.dsSV)

    def Show(self):
        if not self.dsSV:
            print("Danh sach sv rong.")
        else:
            print("Danh sach sv:")
            for sv in self.dsSV:
                print(f"Mã SV: {sv.Ma}, Tên: {sv.Ten}, Năm sinh: {sv.NamSinh}, Điểm TB: {sv.TrungBinh}")

    def Dlt_std(self, masv):
        for sv in self.dsSV:
            if sv.Ma == masv:
                self.dsSV.remove(sv)
                print("Thanh cong.")
                return
        print("Khong tim thay ma.")

    def Editsv(self, masv, new_ten, new_namsinh, new_tb):
        for sv in self.dsSV:
            if sv.Ma == masv:
                if new_ten:
                    sv.Ten = new_ten
                if new_namsinh:
                    sv.NamSinh = new_namsinh
                if new_tb:
                    sv.TrungBinh = new_tb
                print("Thanh cong.")
                return
        print("Khong tim thay ma.")
    def findLan(self):
        cnt =0
        for i in self.dsSV:
            temp = i.split(" ")
            if temp[len(temp)-1].casefold() == "Lan".casefold(): cnt+=1
        return cnt
    def findFirstNamePhan(self):
        cnt =0
        for i in self.dsSV:
            temp = i.split(" ")
            if temp[0].casefold() == "Phan".casefold(): cnt+=1
        return cnt