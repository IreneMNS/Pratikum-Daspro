#Masukkan Nama dan NIM
print('Masukkan Nama,NIM,Kode dengan benar!')
count=0
while count<4:
    Nama = str(input('Masukkan nama :'))
    NIM = int(input('Masukkan NIM :'))
    Kode = str(input('Masukkan kode :'))
    if(Nama=='Irene Miraj Nur Sari' and NIM=='2309116015' and Kode=='pacaritoshirin'):
        print('Hore!Selamat coding!')
        count=5
    else:
        print('waduh!ada kesalahan niee. Coba lagi!')
        count+=1

#Menghitung Segitiga dengan Phytagoras
option = input("Pilih Opsi(1.Hitung sisi tegak, 2.Hitung sisi miring, 3.Hitung sisi Alas):")
if option == "1.Hitung sisi tegak":
    S = int(input("Sisi miring: "))
    A = int(input("Sisi ALas: "))
    T = int(S**2 + A**2)** 0.5
    print(f"Hasil dari T adalah {T}")

elif option == "2.Hitung sisi miring":
    T = int(input("Sisi tegak: "))
    A = int(input("Sisi Alas: "))
    S = int(T**2 + A**2)** 0.5
    print(f"Hasil dari S adalah {S}")

elif option == "3.Hitung sisi Alas":
    T = int(input("Sisi tegak: "))
    S = int(input("Sisi miring: "))
    A = int(S**2 + T**2)** 0.5
    print(f"Hasil dari A adalah {A}")














