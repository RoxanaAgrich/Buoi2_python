"""Viết chương trình Python để tạo một lớp đại diện cho giỏ hàng (ShoppingCart).
Bao gồm các phương pháp thêm (add_item) và xóa (remove_item) các mặt hàng cũng như tính tổng giá (calculate_total).
"""
class Shoppingcart:
    def __init__(self):
        self.items = {}

    def addItem(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
    
    def remove_Item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"{item_name} không có trong giỏ hàng.")
    
    def calculate(self):
        return sum(self.items.values())
    
    
    def display_cart(self):
    
        print("So luong hien co trong gio hang:")
        for item, quantity in self.items.items():
            print(f"{item} - {quantity}")
        print("Tong so luong:", self.calculate())
        
cart = Shoppingcart()

nhap =  int(input("Nhap so luong: "))

for i in range(1, nhap+1, 1):
    sp = input(f"Nhap mat hang thu {i}: ")
    sl = int(input(f"Nhap so luong cua mat hang thu {i}: "))
    cart.addItem(sp, sl)
    
cart.display_cart()

nhapxoa =  int(input("Nhap so luong mat hang de xoa: "))

for i in range(1, nhapxoa + 1):
    sp = input(f"Nhap mat hang thu {i   }: ")
    cart.remove_Item(sp)
    
print("\nCap nhat gio hang sau khi xoa: ")
cart.display_cart()


    
    