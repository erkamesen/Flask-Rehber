from flask_bcrypt import Bcrypt

bcrpyt = Bcrypt()

sifre = "asdfgh"

hashed_sifre = bcrpyt.generate_password_hash(sifre)

print(hashed_sifre)

if bcrpyt.generate_password_hash(hashed_sifre, "asdfgh"):
    print("ŞİFRE DOGRU")

print("-------------------------------------------------------------------------")

from werkzeug.security import generate_password_hash, check_password_hash

while True:
    print("Lütfen 1 yada 2 seçeneğinden birini giriniz.\n1-Kayit Ol\n2-Giriş Yap\n---")
    
    first_choice = input(": ")
    if first_choice == "1":
        kullanici_adi = input("Lütfen kullanici adinizi giriniz: ")
        sifre = input("Lütfen şifrenizi giriniz: ")
        hashlenmis_sifre = generate_password_hash(sifre) # <== #
        with open("kullanici.txt", "a") as f:
            f.write(f"Kullanici Adi: {kullanici_adi}, Sifre: {hashlenmis_sifre}\n")
    elif first_choice == "2":
        with open("kullanici.txt", "r") as f:
            kullanici_listesi = f.readlines()
            kullanici_adi = input("Lütfen kullanici adinizi giriniz: ")
            sifre = input("Lütfen sifrenizi giriniz: ")
            for kullanici in kullanici_listesi:
                kayitli_kullanici_adi = kullanici.split("Sifre: ")[0][15:-2]
                hashli_sifre = kullanici.split("Sifre: ")[1][:-1]
                if kullanici_adi == kayitli_kullanici_adi and check_password_hash(hashli_sifre, sifre): # <== #
                    print("Giriş Yapildi.")
                    break
                else:
                    print("Kullanici Adi yada Sifre Yanlis")
                    break
                
            break
    else:
        print("Hatali islem yaptiniz.")
        break




