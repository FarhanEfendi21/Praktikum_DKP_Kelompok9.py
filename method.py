# KELOMPOK 9 / SHIFT 2
# MUHAMMAD FARHAN EFENDI - 21120123140181
# ESSA BINTANG NUR ATHALLAH - 21120123130067
# A.FAIDHULLAH FARROS BASYKAILLAKH - 21120123140171
# SYAHBANA HATAB - 21120123140180

class metode: #print modal
    #init method
    def __init__(self, harga):
        self.harga = harga

    #self parameter
    def trims(self):
        print("Terimakasih Sudah Menggunakan Program Kelompok 9")

    #method dengan parameter
    def selesai(self, waktu):
        print("Program akan selesai dalam :")
        while waktu > 0:
            print(waktu)
            waktu -= 1
    #
