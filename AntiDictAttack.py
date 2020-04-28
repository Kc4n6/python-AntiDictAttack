import subprocess
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


def kontrol_et():
    subproces = subprocess.Popen("tail -n 3000 /var/log/auth.log", shell=True, stdout=subprocess.PIPE)
    #subprocess.call()
    subprocess_cikti = subproces.stdout.read()
    liste = subprocess_cikti.count("authentication failure")
    if(liste>5):
        Mail_At()
    

def Mail_At():
    mail = MIMEMultipart()
    mail["From"]="kc4n6forensics@gmail.com"
    mail["To"]="kc4n6forensics@gmail.com"
    mail["Subject"]="Server'a saldiri olabilir!!!!"
    Mail_icerigi="son birkaC dakika icerisinde fazla sayida giris denemesi yapildi..."
    icerik = MIMEText(Mail_icerigi,"plain")
    mail.attach(icerik)
    print("buraya kadar sikinti yok kenks")
    try:
        gonder = smtplib.SMTP("smtp.gmail.com",587)
        print("bunu da yaptik kenks")
        gonder.ehlo()
        print("ehlo da tamam kenks")
        gonder.starttls()
        print("tlssi de baslattik kenks")
        gonder.login("kc4n6forensics@gmail.com","Sh1244244b.")
        print("login olduk kenks")
        gonder.sendmail(mail["From"],mail["To"],mail.as_string())
        print("maili de attik kenksss.")
        gonder.close()
    except:
        print("mail gonderme isleminde bir problem var lutfen kontrol saglayiniz.")    


while True:
    timer = threading.Timer(5.0,kontrol_et)
    timer.start()
    timer.join()
    timer.cancel()

