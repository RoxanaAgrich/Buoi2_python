class Wordplay:
    def __init__(self, danh_sach_tu):
        self.danh_sach_tu = danh_sach_tu

    def words_with_length(self, length):
        return [tu for tu in self.danh_sach_tu if len(tu) == length]

    def started_with(self, s):
        return [tu for tu in self.danh_sach_tu if tu.startswith(s)]

    def end_with(self, s):
        return [tu for tu in self.danh_sach_tu if tu.endswith(s)]

    def only(self, L):
        return [tu for tu in self.danh_sach_tu if all(ch in L for ch in tu)]

    def avoids(self, L):
        return [tu for tu in self.danh_sach_tu if all(ch not in L for ch in tu)]

if __name__ == "__main__":
    danh_sach = ["apple", "banana", "grape", "kiwi", "orange", "peach", "plum"]

    wordplay = Wordplay(danh_sach)

    print("Cac tu co do dai 5:", wordplay.words_with_length(5))
    print("Cac tu bat dau bang 'a':", wordplay.started_with('a'))
    print("Cac tu ket thuc bang 'e':", wordplay.end_with('e'))
    print("Cac tu chi chua chu cai trong 'aeiou':", wordplay.only('aeiou'))
    print("Cac tu khong chua chu cai trong 'aeiou':", wordplay.avoids('aeiou'))
