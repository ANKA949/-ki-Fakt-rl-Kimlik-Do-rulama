import smtplib
import random
import sys 
from pyfiglet import Figlet



def index():
    f = Figlet(font='roman')
    print(f.renderText('Giris yaptiniz'))

#mail gönderme
def mail_gonder():
    cod = random.randrange(1,1000000,6) 
    content = str(cod)
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("mail adresinizi girin","şifresi")
    mail.sendmail("mail adresiniz","kime göndereceğinizin mail adresi",content)
    while True:
        giriş = int(input("Mail adresinize gelen doğrulama kodunu girin :"))
        if giriş == cod:
            print("kodunuz doğru")
            index()
            break
        else:
            print("kodunuz hatalı")
#anasayfa
while True:
    print("""
    [1]uygulamaya Giriş
    [2]uygulamadan cıkma
    """)

    secım = int(input("seciminizi Girin :"))
    if secım == 1:
        kullanıcı_adı = input("kullanıcı adınız :")
        kullanıcı_sifre = input("kullanıcı şifreniz :")
        if kullanıcı_adı == "deneme" and kullanıcı_sifre == "1234":
            print("kullanıcı adınız ve şifreniz Doğru ")
            print("Mail adresinize kodunuz gönderiliyor")
            mail_gonder()
        else:
            print("kullanıcı adınız veya şifreniz hatalı")
    elif secım == 2:
        sys.exit()
    else:
        print("hatalı tuslama")
        break