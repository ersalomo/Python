
class Karyawan:
    nama_perusahaan = 'PT. Bersama Kita Hebat'
    insentif_lembur = 250000
    def __init__(self, **kwargs):
        self.__nama = kwargs.get('nama')
        self.__usia = kwargs.get('usia')
        self.__gaji = kwargs.get('gaji')
        self.pendapatan_tambahan = 0
        print(self.display())

    def display(self):
        return 'Nama Karyawan : {}\nUsia\t  :{}\nGaji\t  :{}'.format(self.__nama, self.__usia, self.__gaji)

    def lembur(self):
        self.__gaji +=self.insentif_lembur

    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan +=nilai_proyek
    def getGaji(self):
        return self.__gaji

    def tot_pendapatan(self):
        return self.__gaji + self.pendapatan_tambahan

class Perusahaan:
    def __init__(self, nama, alamat,no_telp):
        self.nama_perusahaan  = nama
        self.alamat = alamat  
        self.no_telp = no_telp
        self.list_karyawan = []

    def tambahan_karyawan(self, nama_karywan):
        self.list_karyawan.append(nama_karywan)

    def nonaktifan_karyawan(self, nama_karywan):
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karywan:
                karyawan_nonaktif = karyawan
                break
        if karyawan_nonaktif is not None:
            self.list_karyawan.append(karyawan_nonaktif)
    def getKaryawan(self):
        return len(self.list_karyawan)

class Admin(Karyawan):
    def __init__(self,**kwargs):
        # super().__init__()jika kosong maka data Class Admin  None
        super().__init__(**kwargs)
        self.__nama =kwargs.get('nama')
        self.__usia = kwargs.get('usia')
        self.__gaji = kwargs.get('gaji')
        self.__hobi = kwargs.get('hobi')
        print(self.getHobi())
    def getHobi(self):
        return 'Hobbi\t:{}\n'.format(self.__hobi)

jonas = Karyawan(nama="Jonas",usia=21,gaji=600000)
print()
ersalomo = Admin(nama="Ersalomo", usia=20, gaji=600000,hobi='administrator')
agung = Admin(nama="Agung", usia=20, gaji=100000,hobi='administrator')

pt_makmur = Perusahaan("PT Abadi",'Jl. Merdeka lalap 29','+20920118') 


pt_makmur.tambahan_karyawan(jonas)
pt_makmur.tambahan_karyawan(ersalomo)
pt_makmur.tambahan_karyawan(agung)
print(pt_makmur.getKaryawan())