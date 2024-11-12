def tongchan():
    n = int(input("Nhap n:"))
    i = 0
    tong = 0
    while i <= n:
        if( i % 2 == 0):
            tong += i
        i+=1
    print(tong)
tongchan()

