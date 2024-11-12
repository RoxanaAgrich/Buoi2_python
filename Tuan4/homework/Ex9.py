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
        self.Ten = ten  # Sửa lỗi dấu '-' thành '='
        self.NamSinh = namsinh
        self.TrungBinh = tb

    def is_qualified(self):
        return self.TrungBinh >= 5

    def is20(self):
        current_year = datetime.now().year
        return current_year - self.NamSinh >= 20

    def isDH(self):
        return self.Ma[2:4] == "DH"


class SinhVienManager:
    def __init__(self):
        self.danh_sach_sv = []

    def Add_std(self, masv, ten, namsinh, tb):
        sinh_vien = SinhVien(masv, ten, namsinh, tb)
        self.danh_sach_sv.append(sinh_vien)

    def svdudieukien(self):
        return sum(sv.is_qualified() for sv in self.danh_sach_sv)

    def xuat_sv_20_tuoi(self):
        sv_20_tuoi = [sv for sv in self.danh_sach_sv if sv.is20()]
        return sv_20_tuoi

    def dem_sv_dh(self):
        return sum(sv.isDH() for sv in self.danh_sach_sv)

    def xem_danh_sach(self):
        if not self.danh_sach_sv:
            print("Danh sách sinh viên trống.")
        else:
            print("Danh sách sinh viên:")
            for sv in self.danh_sach_sv:
                print(f"Mã SV: {sv.Ma}, Tên: {sv.Ten}, Năm sinh: {sv.NamSinh}, Điểm TB: {sv.TrungBinh}")

    def xoa_sinh_vien(self, masv):
        for sv in self.danh_sach_sv:
            if sv.Ma == masv:
                self.danh_sach_sv.remove(sv)
                print("Xóa sinh viên thành công.")
                return
        print("Không tìm thấy sinh viên với mã này.")

    def Editsv(self, masv, new_ten=None, new_namsinh=None, new_tb=None):
        for sv in self.danh_sach_sv:
            if sv.Ma == masv:
                if new_ten:
                    sv.Ten = new_ten
                if new_namsinh:
                    sv.NamSinh = new_namsinh
                if new_tb:
                    sv.TrungBinh = new_tb
                print("Sửa thông tin sinh viên thành công.")
                return
        print("Không tìm thấy sinh viên với mã này.")
    def findLan(self):
        cnt =0
        for i in self.danh_sach_sv:
            temp = i.split(" ")
            if temp[len(temp)-1].casefold() == "Lan".casefold(): cnt+=1
        return cnt
    def findFirstNamePhan(self):
        cnt =0
        for i in self.danh_sach_sv:
            temp = i.split(" ")
            if temp[0].casefold() == "Phan".casefold(): cnt+=1
        return cnt