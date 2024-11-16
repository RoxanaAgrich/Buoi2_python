class DanhSach:
    def __init__(self):
        # khoi tao ds rong
        self.danh_sach = []

    def them_phan_tu(self, phan_tu):
        self.danh_sach.append(phan_tu)
        print(f"da them pt: {phan_tu}")

    def xoa_phan_tu(self, phan_tu):
        if phan_tu in self.danh_sach:
            self.danh_sach.remove(phan_tu)
            print(f"da xoa pt: {phan_tu}")
        else:
            print(f"pt {phan_tu} ko ton tai trong ds.")

    def hien_thi_danh_sach(self):
        if self.danh_sach:
            print("cac pt trong ds:")
            for i, phan_tu in enumerate(self.danh_sach, start=1):
                print(f"{i}. {phan_tu}")
        else:
            print("ds rong")

    def lay_danh_sach(self):
        return self.danh_sach

if __name__ == "__main__":
    danh_sach = DanhSach()

    while True:
        print("1. them pt vao ds")
        print("2. xoa pt khoi ds")
        print("3. In ds ket qua")
        print("4. thoat")

        lua_chon = input("nhap lua chon (1-5): ")

        if lua_chon == "1":
            phan_tu = input("nhap pt can them: ")
            danh_sach.them_phan_tu(phan_tu)

        elif lua_chon == "2":
            phan_tu = input("nhap pt can xoa: ")
            danh_sach.xoa_phan_tu(phan_tu)

        elif lua_chon == "3":
            danh_sach.hien_thi_danh_sach()

        elif lua_chon == "5":
            print("thoat chuong trinh.")
            break

        else:
            print("Lua chon khong hop le.")




