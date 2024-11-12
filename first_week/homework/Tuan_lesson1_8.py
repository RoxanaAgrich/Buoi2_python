'''8. Những năm nào chia hết cho 4 được và không chia hết cho 100 được coi là năm nhuận (ví dụ năm 
2100 không phải là năm nhuận, 2104 là năm nhuận). Viết chương trình hỏi người dùng một năm và 
in ra xem đó có phải là năm nhuận hay không? '''

def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

year = int(input("Nhap nam: "))

if is_leap_year(year):
    print(f"{year} la nam nhuan")
else:
    print(f"{year} khong la nam nhuan")

