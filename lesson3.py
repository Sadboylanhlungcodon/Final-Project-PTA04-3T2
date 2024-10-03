class HocSinh:
    def __init__(self, _hoten, _lop, _truong, _diemtoan, _diemvan, _diemanh):
        self.hoten = _hoten
        self.lop = _lop
        self.truong = _truong
        self.diemtoan = _diemtoan
        self.diemvan = _diemvan
        self.diemanh = _diemanh

    def GPA(self):
        return(self.diemtoan + self.diemvan + self.diemanh) / 3
    def getName(self):
        print(self.hoten)

class QuanLyHs:
    def __init__(self):
        hs1 = HocSinh("Nguyễn A", "PTA04", 10, 10, 10)
        hs2 = HocSinh("Nguyễn B", "PTA04", 9, 9, 9)
        hs3 = HocSinh("Nguyễn C", "PTA04", 8, 8, 8)
        self.dshocsinh = [hs1, hs2, hs3]


exit()
class PhanSo:
    # ham khoi tao
    def __init__(self, _tuso = 0, _mauso = 1):
        self.tuso = _tuso
        self.mauso = _mauso
    # ham nhap
    def _input(self):
        l = input().split()
        self.tuso = int(l[0])
        self.mauso = int(l[1])
    # ham xuat
    def _output(self):
        print(str(self.tuso) + "/" + str(self.mauso))
    def XuatTuSo(self):
        print(self.tuso)
    def XuatMauSo(self):
        print(self.mauso)
    def XuatPhanSoNghichDao(self):
        print(str(self.mauso) + "/" + str(self.tuso))
    def PhanSoRutGon(self):
        tumoi, maumoi = self.tuso, self.mauso
        mauchung = 2
        while tumoi >= mauchung and maumoi >= mauchung:
            while tumoi % mauchung == 0 and maumoi % mauchung == 0:
                tumoi /= mauchung
                maumoi /= mauchung
            mauchung += 1

        return PhanSo(int(tumoi), int(maumoi))
    def TongVoiPhanSoNghichDao(self):
        a = self.tuso
        b = self.mauso
        
        tusomoi = a*a + b*b
        mausomoi = a*b

        return PhanSo(tusomoi, mausomoi).PhanSoRutGon()._output()
ps = PhanSo()
ps._input()
ps._output()
ps.XuatTuSo()
ps.XuatMauSo()
ps.XuatPhanSoNghichDao()
ps.PhanSoRutGon()._output()
ps.TongVoiPhanSoNghichDao()

exit()
class xe:
    #hàm khởi tạo
    def __init__(self, _hangxe = "chưa biết", _mauxe = "chưa biết", _giaxe = "chưa biết"):
        self.hangxe = _hangxe
        self.mauxe = _mauxe
        self.giaxe = _giaxe
    #Hàm in ra thông tin
    def show(self):
        print("Hãng xe", self.hangxe)
        print("Màu xe", self.mauxe)
        print("Giá xe", self.giaxe)

#Trường hợp chưa nhập
xe1 = xe()
xe1.show()
#Trường hợp đã nhập
xe2 = xe("Vinfast", "Trắng", 1000)
xe2.show()