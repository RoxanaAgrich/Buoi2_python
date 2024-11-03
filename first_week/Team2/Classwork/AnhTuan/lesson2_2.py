''' Viết hàm trộn 2 mảng một chiều thành 1 mảng một chiều với mỗi phần tử của mảng mới 
là tổng của 2 phần tương ứng từ 2 mảng cho trước. Trong quá trình trộn 2 mảng nếu mảng 
nào còn phần tử thì các phần tử còn lại của mảng đó sẽ đưa vào mảng mới. 
Ví dụ: 
Mảng a: 3 9 1 4 
Mảng b: 2 7 4 3 2 8 
Mảng kết quả: 5 16 5 7 2 8. '''

def tron_mang(a, b):
    max_len = max(len(a), len(b))
    ket_qua = []
    
    for i in range(max_len):
        # ktra ptu o vtri i co thuoc a hay ko
        phan_tu_a = a[i] if i < len(a) else 0
        # ktra ptu o vtri i co thuoc b hay ko
        phan_tu_b = b[i] if i < len(b) else 0
        
        # Them tong cua 2 pt vao mang kq
        ket_qua.append(phan_tu_a + phan_tu_b)
    
    return ket_qua

a = [3, 9, 1, 4]
b = [2, 7, 4, 3, 2, 8]

ket_qua = tron_mang(a, b)
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng kết quả:", ket_qua)

