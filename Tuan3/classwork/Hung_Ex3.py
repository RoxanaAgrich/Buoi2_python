# Bài 3. Viết một chương trình để tạo một lớp và lấy tất cả các tập hợp con riêng biệt 
# có thể
# có từ một tập hợp các số nguyên riêng biệt.
# Yêu cầu:
# 1. Tạo một lớp và định nghĩa hai phương thức trong lớp: 
#  Phương thức f1 được sử dụng để chuyển một danh sách trống và danh sách đã sắp 
# xếp được lấy từ người dùng sang phương thức f2.
#  Phương pháp f2 được sử dụng để tính toán tất cả các tập hợp con có thể có của danh 
# sách.
# 2. In ra kết quả các tập hợp con có thể có của danh sách
# 3. Thoát
class Taphop:
    def __init__(self, lst):
        self.TapHop = lst
        self.SoLuong = len(lst)
    
    def f2(self, nums, index, TaphopHientai, result):
        result.append(TaphopHientai[:])
        for i in range(index, self.SoLuong):
            TaphopHientai.append(nums[i])
            self.f2(nums, i + 1, TaphopHientai, result)
            TaphopHientai.pop()
    
    def f1(self):
        result = []
        self.f2(self.TapHop, 0, [], result)
        return result

a = (input("Tap hop: ")).strip().split(" ")
a= [int(i) for i in a]
tap_hop = Taphop(a)
Taphopcon = tap_hop.f1()
print("Các tập hợp con của", tap_hop.TapHop, "là:", Taphopcon)
