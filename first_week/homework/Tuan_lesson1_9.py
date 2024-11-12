# Hinh chu nhat day
long = int(input("Nhap chieu dai: "))
width = int(input("Nhap chieu rong: "))

for i in range(width):
    print('* ' * long)

# Hinh chu nhat rong
long = int(input("Nhap chieu dai: "))
width = int(input("Nhap chieu rong: "))

for i in range(width):
    if i == 0 or i == width - 1:
        print('* ' * long)
    else:
        print('* ' + '  ' * (long - 2) + '*')

# Nua phai hinh tam giac
height = int(input("Nhap chieu cao cua tam giac: "))

for i in range(1, height + 1): # Mac dinh cua end là n - 1 nhung vi start tai 1 (neu start = 0 thi se tao ra khoang trong vo nghia) nen end phai + 1 de can bang voi start
    print('*' * i) # 'x ' se nhin thay ro hon bang mat thuong la tg vuong can x = y = i

# Hinh thoi
height = int(input("Nhap chieu cao cua hinh thoi: "))
for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * (2 * i - 1))
for i in range(height - 1, 0, -1): # Start height - 1 de tranh bi trung lap voi for cua tg dau tien
    print(' ' * (height - i) + '*' * (2 * i - 1)) # For nguoc de xuat tg con lai


