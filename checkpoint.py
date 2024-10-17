# 1.D
# 2.C
# 3.A
# 4.B
# 5.D
# 6.A
# 7.B
# 8.B
# 9.B
# 10.B

class HocSinh:
    def __init__(self, _hovaten = "chưa biết", _diachi = "chưa biết", _chieucao = "chưa biết", _cannang = "chưa biết", _hocluc = "chưa biết"):
        self.hovaten = _hovaten
        self.diachi = _diachi
        self.chieucao = _chieucao
        self.cannang = _cannang
        self.hocluc = _hocluc

    def chuyennha(self, _diachinhamoi):
        self.diachi = _diachinhamoi
        
    def khamsuckhoe(self, _chieucaomoi, _cannangmoi):
        self.chieucao = _chieucaomoi
        self.cannang = _cannangmoi

    def show(self):
        print("Tên học sinh:", self.hovaten)
        print("Địa chỉ:", self.diachi)
        print("chiều cao:", self.chieucao)
        print("Cân nặng:", self.cannang)
        print("Học lực:", self.hocluc)
    
hs1 = HocSinh("Lê Hồng Quân", "Sài Gòn", "150 cm", "50 kg", "xuất xắc đạt 5 giải Nobel vật lí, 2 giải Nobel toán học, 8 giải Nobel tin học, 15 huy chương vàng Olympic vàng Olympic")
hs1.show()

hs1.chuyennha("Biệt thự bên sao hỏa")
hs1.khamsuckhoe("170 cm", "60 kg")
hs1.show()