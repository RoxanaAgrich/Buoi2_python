#Một cửa hàng tính phí 12 USD cho mỗi mặt hàng nếu bạn mua ít hơn 10 mặt hàng.
#Nếu bạn mua từ 10 đến 99 các mặt hàng, chi phí là $10 cho mỗi mặt hàng. Nếu bạn mua 100 món trở lên, giá là 7$ một món.
#Viết một chương trình hỏi người dùng họ đang mua bao nhiêu mặt hàng và in tổng chi phí.

tong = 0
while True:
    n = int(input("Nhap so luong mat hang: "))
    if n > 0:
        break
    print("Hay nhap lai, so luong phai lon hon 0!")
        

if n < 10:
    tong = n * 12
    print("Tong chi phi: ", tong)
elif n >= 10 and n < 99:
    tong = n * 10
    print("Tong chi phi: ", tong)
elif n >= 100:
    tong = n * 7
    print("Tong chi phi: ", tong)
