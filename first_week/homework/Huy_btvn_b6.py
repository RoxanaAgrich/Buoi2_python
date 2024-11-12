# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200).
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
n = range(2000, 3200)
for a in n:
    if a % 7 == 0 and a % 5 != 0:
        print("%d" % a, end= ",")