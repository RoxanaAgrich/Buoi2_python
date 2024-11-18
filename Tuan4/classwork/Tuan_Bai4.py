"""Viết một lớp có tên là Sản phẩm. Lớp này phải có các thuộc tính: số lượng và giá, tên 
sản phẩm, số lượng mặt hàng của sản phẩm đó trong kho và giá thông thường của sản phẩm.

Cần có một phương thức get_price để nhận số lượng mặt hàng cần mua và trả về chi phí mua nhiều mặt hàng đó.
Trong đó giá thông thường được tính cho các đơn hàng dưới 10 mặt hàng, áp dụng giảm giá 10% cho các đơn hàng
từ giữa 10 và 99 mặt hàng, giảm giá 20% cho đơn hàng từ 100 mặt hàng trở lên. 
Cũng nên có một phương thức gọi là make_purchase để nhận số lượng mặt hàng cần mua và giảm số lượng đó đi."""

class SanPham:
    def __init__(self, ten, gia_thong_thuong, so_luong_trong_kho):
        self.ten = ten
        self.gia_thong_thuong = gia_thong_thuong
        self.so_luong_trong_kho = so_luong_trong_kho

    def get_price(self, so_luong_mua):
        if so_luong_mua < 10:
            gia = self.gia_thong_thuong * so_luong_mua
        elif 10 <= so_luong_mua <= 99:
            gia = self.gia_thong_thuong * so_luong_mua * 0.9
        else:
            gia = self.gia_thong_thuong * so_luong_mua * 0.8
        
        return round(gia, 2) # lam tron 2 chu so thap phan

    def make_purchase(self, so_luong_mua):
        # giam so luong sp trong kho sau khi da duoc mua
        if so_luong_mua <= self.so_luong_trong_kho:
            self.so_luong_trong_kho -= so_luong_mua
            print(f"da mua {so_luong_mua} {self.ten}. con lai {self.so_luong_trong_kho} trong kho.")
        else:
            print(f"ko du sl {self.ten} trong kho. hien tai con {self.so_luong_trong_kho}.")

    def hien_thi_thong_tin(self):
        print(f"ten sp: {self.ten}")
        print(f"gia niem yet: {self.gia_thong_thuong}")
        print(f"sl trong kho: {self.so_luong_trong_kho}")

if __name__ == "__main__":
    san_pham = SanPham("quan tay", 100, 150)

    while True:
        print("1. hien thi tt sp")
        print("2. tinh gia mua sp (bao gom giam gia mua sl)")
        print("3. mua sp")
        print("4. thoat")

        lua_chon = input("nhap lua chon (1-4): ")

        if lua_chon == "1":
            san_pham.hien_thi_thong_tin()

        elif lua_chon == "2":
            so_luong = int(input("nhap sl sp can mua: "))
            gia = san_pham.get_price(so_luong)
            print(f"gia cua {so_luong} sp la: {gia}")

        elif lua_chon == "3":
            so_luong = int(input("nhap sl sp can mua: "))
            san_pham.make_purchase(so_luong)

        elif lua_chon == "4":
            print("thoat chuong trinh.")
            break

        else:
            print("lua chon ko hop le.")
