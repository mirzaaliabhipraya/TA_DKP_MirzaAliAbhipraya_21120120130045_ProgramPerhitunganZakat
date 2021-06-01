
class dataNama():
    input_nama,input_pekerjaan,keterangan = "","",""
    input_umur,input_emas,input_penghasilan,penghasilan_tahun,zakat,nisab = 0,0,0,0,0,0
    def __init__(self, input_nama, input_umur, input_pekerjaan, input_penghasilan, input_emas, penghasilan_tahun, keterangan, zakat, nisab):
        self.input_nama = input_nama
        self.input_umur = input_umur
        self.input_pekerjaan = input_pekerjaan
        self.input_penghasilan = input_penghasilan
        self.input_emas = input_emas
        self.penghasilan_tahun = penghasilan_tahun
        self.keterangan = keterangan
        self.zakat = zakat
        self.nisab = nisab
    def setData(self,input_nama, input_umur, input_pekerjaan,input_penghasilan,input_emas):
        self.input_nama = input_nama
        self.input_umur = input_umur
        self.input_pekerjaan = input_pekerjaan
        self.input_penghasilan = input_penghasilan
        self.input_emas = input_emas
        pass
    def hitung(self):
        self.penghasilan_tahun = 12 * self.input_penghasilan
        self.zakat = 0.025 * self.penghasilan_tahun
        self.nisab = 85 * self.input_emas
        if self.penghasilan_tahun>self.nisab:
            self.keterangan = "Wajib Zakat"
        else:
            self.keterangan = "Tidak Wajib Zakat"
    def getpenghasilantahun(self):
        return self.penghasilan_tahun
    def getzakat(self):
        return self.zakat
    def getnisab(self):
        return self.nisab
    def getketerangan(self):
        return self.keterangan
    def getnama(self):
        return self.input_nama
    def getumur(self):
        return self.input_umur
    def getpekerjaan(self):
        return self.input_pekerjaan
    
