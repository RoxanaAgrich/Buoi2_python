from math import sqrt


def Ptb2():
    a = float(input("Nhap a:"))
    b = float(input("Nhap b:"))
    c = float(input("Nhap c:"))
    delta = pow(b,2) - 4 * a * c
    if(delta > 0):
        x1 = (- b + sqrt(delta)) / 2 * a
        x2 = (- b - sqrt(delta)) / 2 * a
        print(f"Phuong trinh co 2 nghiem phan biet:\nx1 = {x1}\nx2 = {x2}")
    elif(delta == 0):
        x1 = -b / 2 * a
        print(f"Phuong trinh co nghiem kep:\nx = {x1}")
    else:
        print("Phuong trinh vo nghiem")
Ptb2()
