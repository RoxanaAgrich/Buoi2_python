'''Yêu cầu người dùng nhập nhiệt độ bằng độ C. 
Chương trình sẽ in một tin nhắn dựa trên
về nhiệt độ:
 Nếu nhiệt độ nhỏ hơn -273,15, 
in ra rằng nhiệt độ không hợp lệ vì nó dưới độ không 
tuyệt đối.
 Nếu chính xác là -273,15, in ra nhiệt độ tuyệt đối bằng 0.
 Nếu nhiệt độ nằm trong khoảng từ -273,15 đến 0, in ra nhiệt 
độ dưới điểm đóng băng.
 Nếu bằng 0, in ra nhiệt độ đang ở điểm đóng băng.
 Nếu nằm trong khoảng từ 0 đến 100, in ra nhiệt độ
ở mức bình thường.
 Nếu là 100, in ra nhiệt độ đang ở điểm sôi.++
 Nếu trên 100, in ra nhiệt độ cao hơn điểm sôi'''

def temperature(c):
    if c < -273.15: 
        return "Nhiệt độ không hợp lệ vì nó dưới độ không tuyệt đối"
    elif c==-273.15: 
        return "Nhiệt độ dưới điểm đóng băng"
    elif c > -273.15 and c < 0: 
        return "Nhiệt độ dưới điểm đóng băng."
    elif c == 0 : 
        return "Nhiệt độ đang ở điểm đóng băng"
    elif c>0 and c<100: 
        return "Nhiệt độ ở mức bình thường"
    elif c == 100 :
        return "Nhiệt độ đang ở điểm sôi"
    elif c>100: 
        return "Nhiệt độ cao honw điểm sôi"

if __name__ == "__main__":
    a = int (input ("Nhap nhiet do: "));
    print(temperature(a));