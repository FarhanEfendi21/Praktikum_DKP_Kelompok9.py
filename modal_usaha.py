from method import *

def listBaju(): #fungsi list baju no return
    print("""
    -- Selamat Datang di Program Kelompok 9 --

    --------------------------------------     
    Simulasi Harga Modal Usaha Pakaian 
    Daftar list pakaian dan harga (/pcs)
    1 : Kaos\t\t - Rp. 35.000
    2 : Kaos Polo\t - Rp. 40.000   
    3 : Kemeja\t\t - Rp. 60.000
    4 : Baju Batik\t - Rp. 65.000
    5 : Celana\t\t - Rp. 70.000
    6 : Rok\t\t - Rp. 55.000
          
    --------------------------------------  

    Spesial Item : 
    7 : Hoodie\t\t - Rp. 80.000
    8 : Varsity\t\t - Rp. 100.000       
    0 : Batal
    --------------------------------------  
    """)

def opsiBaju(opsi): #fungsi opsi baju dengan return berparameter
    switcher={
        1 : "Kaos\t - Rp. 35.000",
        2 : "Kaos Polo\t - Rp. 40.000",  
        3 : "Kemeja\t - Rp. 60.000",
        4 : "Baju Batik\t - Rp. 65.000",
        5 : "Celana\t - Rp. 70.000",
        6 : "Rok\t - Rp. 55.000",
        7 : "Hoodie\t - Rp. 80.000",
        8 : "Varsity\t - Rp. 100.000",
        0: "Program selesai",
        }
    return switcher.get(opsi, "Kode tersebut salah")


def hargaBaju(opsi): #fungsi harga baju dengan return berparameter
    if opsi == int(1):
        harga = int(35000)
        return harga
    elif opsi == 2:
        harga = int(40000)
        return harga
    elif opsi == 3:
        harga = int(60000)
        return harga
    elif opsi == 4:
        harga = int(65000)
        return harga
    elif opsi == 5:
        harga = int(70000)
        return harga
    elif opsi == 6:
        harga = int(55000)
        return harga
    elif opsi == 7:
        harga = int(80000)
        return harga
    elif opsi == 8:
        harga = int(100000)
        return harga
    else:
        print("Opsi anda salah! ")


def totalModal():
    global total 
    total = 0
    while True:
        listBaju()
        a = int(input("Masukkan kode baju : "))
        print(opsiBaju(a))
        list = [opsiBaju(a)]
        q = int(input("Masukkan kuantitas baju : "))
        totalAwal = hargaBaju(a) * q
        total = total + totalAwal
        print("Total harga modal baju : ", total)
        lanjut = int((input("Apakah anda masih ingin menambahkan baju lagi? : (1. Ya/ 0. Tidak) : ")))
        if lanjut != 1:
            print("Total harga modal baju : " , total)
            break

    return total

def diskon(totalByr):
    if totalByr > 200000:
            totalByr = totalByr * 0.95 #diskon 5%
    elif totalByr > 500000:
            totalByr = totalByr * 0.90 #diskon 10%
    elif totalByr > 1000000:
            totalByr = totalByr * 0.20 #diskon 20%
    else:
            totalByr = totalByr
    return totalByr



panggil = metode(totalModal())
print("total harga dengan diskon : " , diskon(total))
panggil.trims()
panggil.selesai(5)
input("Tekan Enter untuk keluar")



