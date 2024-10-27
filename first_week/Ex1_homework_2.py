# Viết hàm trộn 2 mảng một chiều thành 1 mảng một chiều với mỗi phần tử của mảng mới 
# là min của 2 phần tương ứng từ 2 mảng cho trước. Trong quá trình trộn 2 mảng nếu mảng 
# nào còn phần tử thì các phần tử còn lại của mảng đó sẽ đưa vào mảng mới.

a = list(input("Nhập mảng 1:").split(" "))
a = [int (i) for i in a]
b = list(input("Nhập mảng 2:").split(" "))
b = [int (i) for i in b]
c= []
maxlenght = a if len(a)>len(b) else b
for i in range(len(maxlenght)):
    if (i<len(a if len(a)<len(b) else b)-1) :
        c.append(min(a[i],b[i]))
    else: c.append(maxlenght[i])
    
print ("Mang su khi tron: ",c);