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
        return 'Nama Karyawan : {}\nUsia   \t  :{}\nGaji   \t  :{}'.format(self.__nama, self.__usia, self.__gaji)

    def lembur(self):
        self.__gaji +=self.insentif_lembur

    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan +=nilai_proyek

    def getGaji(self):
        return self.__gaji

    def getName(self):
        return self.__nama

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
        # tidak terpakai
        # self.__nama =kwargs.get('nama')
        # self.__usia = kwargs.get('usia')
        # self.__gaji = kwargs.get('gaji')
        self.__hobi = kwargs.get('hobi')
        print(self.getHobi())
    def getHobi(self):
        return 'Occupation\t:{}\n'.format(self.__hobi)

class Dokter(Karyawan):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__specialis = kwargs.get('specialis')
        print(self.getJob())

    def getJob(self):
        return 'Hobbi\t:{}\n'.format(self.__specialis) 
    
    def tambahan_proyek(self, value_of_proyek):
        self.pendapatan_tambahan +=value_of_proyek*0.2

    

class salesAdmin(Admin):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    # kita harus mendefinisikan staticmethod agar dapat mengakses kelas parent
    @classmethod
    def getLocation(cl):
        return cl.nama_perusahaan

    @classmethod
    def coba(cls):
        return cls.insentif_lembur


jonas = Karyawan(nama="Jonas",usia=21,gaji=600000)
print()
ersalomo = Admin(nama="Ersalomo", usia=20, gaji=600000,hobi='administrator')
agung = Admin(nama="Agung", usia=20, gaji=100000,hobi='administrator')

selena = Dokter(nama="Selena", usia=22, gaji=10000000,specialis="kandungan")
yakamura = salesAdmin(nama="yakamura", usia=19, gaji=12000000)

pt_makmur = Perusahaan("PT Abadi",'Jl. Merdeka lalap 29','+20920118') 
pt_makmur.tambahan_karyawan(jonas)
pt_makmur.tambahan_karyawan(ersalomo)
pt_makmur.tambahan_karyawan(agung)

print('')
selena.lembur()
selena.tambahan_proyek(100000)
print(f'Total gaji {jonas.getName()} : {jonas.tot_pendapatan()}')
print(f'Total gaji {ersalomo.getName()} : {ersalomo.tot_pendapatan()}')
print(f'Total gaji {agung.getName()} : {agung.tot_pendapatan()}')
print(f'Total gaji {selena.getName()} : {selena.tot_pendapatan()}')

print(f'bio data {yakamura.getName()} bekerja di {yakamura.getLocation()}')
print(yakamura.coba())
