# Câu 1: Xây dựng lớp người (Person). Bao gồm các thuộc tính như tên, quốc gia, và ngày sinh và các phương thức:
# - Xác định tuổi của người đó
# - In ra thông tin của người đó
# - Xây dựng file input.json bao gồm mảng thông tin của nhiều người. Mỗi người gồm các thuộc tính: name, country, birthday
# - Đọc file này thành một list của các đối tượng Person.
# - Xây dựng chức năng: Thêm một người vào danh sách, Xóa người dựa trên tên, Xuất ra danh sách người có tuổi cho trước.
# - Xử lý lỗi khi cần thiết.

import json

from datetime import datetime

class Person:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def calculated_age(self):
        birth_age = datetime.strptime(self.birthday, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_age.year - ((today.month, today.day) < (birth_age.month, birth_age.day)) 
        return age
    
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Country: {self.country}\n"
                f"Date of Birth: {self.birthday}\n"
                f"Age: {self.calculated_age()}")
    
def load_json(file_path):
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                return [Person(person["name"], person["country"], person["birthday"]) for person in data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading file Json: {e}")
            return []
    
def save_people_to_json(file_path, people):
        with open(file_path, 'w', encoding="utf-8") as file:
            json.dump([{"name": person.name, "country": person.country, "birthday": person.birthday} for person in people], file, ensure_ascii=False, indent=4)

def add_people(people, name, country, birthday):
        people.append(Person(name, country, birthday))

def remove_people(people, name):
        for person in people:
            if person.name == name:
                people.remove(person)
                return True
        return False
    
def filter_people_by_age(people, age):
        return [person for person in people if person.calculated_age() == age]
    
if __name__ == "__main__":
    file_path = "E:\Code Python\Project\Buoi2_python\Tuan6\Data\homework\dataEx1.json"

    people = load_json(file_path)

    add_people(people, "Nam", "Việt Nam", "2005-01-01")

    print("Danh sách mọi người: ")
    for i, person in enumerate(people, start=1):
        print(f"\nPerson {i}: \n{person}")

    save_people_to_json(file_path, people)

    name_to_remove = input("Nhập tên người cần xóa: ")
    if remove_people(people, name_to_remove):
        print(f"\nĐã xóa người tên {name_to_remove}")
    else:
        print(f"\nKhông tìm thấy người tên {name_to_remove} ")


    age_to_filter = int(input("Nhập tuổi: "))
    filtered_people = filter_people_by_age(people, age_to_filter)
    print(f"\nDanh sách những người {age_to_filter} tuổi:")
    for person in filtered_people:
        print(person)


