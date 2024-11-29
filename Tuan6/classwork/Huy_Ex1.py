import csv

#Mở file để đọc
def read_input_file(filename):
    try:
        with open('Huy_Ex1_input.txt', 'r') as file:
            content = file.readlines()
    
            if not content:  # Kiểm tra nếu file rỗng
                raise ValueError("File không có dữ liệu.")
    
            numbers = [int(line.strip()) for line in content if line.strip().isdigit()]
            return numbers

    except FileNotFoundError:
        raise FileNotFoundError("File không tồn tại.")
    except Exception as e:
        raise Exception(f"Lỗi không xác định")
            
#Tính tổng
def calculate(numbers):
    total = sum(numbers)
    return total

try:
# Đọc dữ liệu từ file
    numbers = read_input_file('Huy_Ex1_input.txt')

# Tính tổng
    result = calculate(numbers)
    
#Mở file để ghi nội dung         
    with open('Huy_Ex1_output.txt', 'w') as output_file:
        output_file.write(f"Tong cac so la: {result}\n")
        print("Ghi kết quả thành công.")
except Exception as e:
    print(e)