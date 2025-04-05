import requests
from bs4 import BeautifulSoup
import time
import re

class Hisse:
    def __init__(self):
        self.dongu=True



    def program(self):
        secim=self.menu()
        
        if secim =="1":
            print("Guncel fiyatlar aliniyor...\n")
            time.sleep(3)
            self.guncelfiyat()
        
        if secim =="2":
            print("Künye bilgileri aliniyor...\n")
            time.sleep(3)
            self.kunye()
        
        if secim =="3":
            print("Cari degerler aliniyor...\n")
            time.sleep(3)
            self.carideger()

                    
        if secim =="4":
            print("Getiri bilgileri aliniyor...\n")
            time.sleep(3)
            self.getiri()
        
        if secim =="5":
            print("Endeks agirlik oranlari aliniyor...\n")
            time.sleep(3)
            self.dahilendeks()
        
        if secim =="6":
            print("Otomasyondan cikiliyor...")
            time.sleep(3)
            self.cikis()




    def menu(self):
        def kontrol(secim):
            if not re.search("[1-6]",secim):
                raise Exception("Lutfen 1 ve 6 arasinda gecerli bir seçim yapiniz.")
            elif len(secim)!=1:
                raise Exception("Lutfen 1 ve 6 arasinda gecerli bir seçim yapiniz.")
    


        while True:
            try:
                secim=input("""\nOtomasyon sistemine hosgeldiniz.\n\n
Lutfen yapmak istediginiz islemi seciniz:
[1]-Guncel Fiyat
[2]-Sirket Kunyesi
[3]-Cari Degerler
[4]-Getiri Rakamlari
[5]-Sirketin Dahil Oldugu Endeksler
[6]-Çikis\n""")
                kontrol(secim)
            
            
            except Exception as hata:
                print(hata)
                time.sleep(3)
            
            else:
                break
        return secim



    
    def guncelfiyat(self):
        while True:
            try:
                sirket = input("Lutfen sirket adi giriniz: ")

                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx"

                parser = BeautifulSoup(requests.get(url).content,"html.parser")

                fiyat = parser.find("a",{"href":"/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket.upper())})\
                .parent.parent.find_all("td")

 #parent = bir ust etikete gorurur.

                bilgi1 = fiyat[1].string
                bilgi2 = fiyat[2].span.string
                bilgi3 = fiyat[3].string
                bilgi4 = fiyat[4].string
                bilgi5 = fiyat[5].string
               
                print(f"""
Son Fiyat: {bilgi1}
Degisim(%): {bilgi2.lstrip()}\rDegisim(TL):{bilgi3}
Hacim(TL): {bilgi4}
Hacim(Adet): {bilgi5}""")
                break


            except AttributeError:
                print("Hatali bir sirket adi girdiniz")
                time.sleep(3)
        time.sleep(3)
        self.menudon()

                


    def kunye(self):
        while True:
            try:
                sirket = input("Lutfen sirket adi giriniz: ")

                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)

                parser = BeautifulSoup(requests.get(url).content,"html.parser")

                kunye = parser.find("div",{"id":"ctl00_ctl58_g_6618a196_7edb_4964_a018_a88cc6875488"})\
                .find_all("tr")

                for i in kunye:
                    bilgi1 = i.th.string
                    bilgi2 = i.td.string
                    print(f"{bilgi1} : {bilgi2}")
                break

            except AttributeError:
                print("Hatali bir sirket adi girdiniz")
                time.sleep(3)
        time.sleep(3)
        self.menudon()

                

    
    def carideger(self):
        while True:
            try:
                sirket = input("Lutfen sirket adi giriniz: ")

                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)

                parser = BeautifulSoup(requests.get(url).content,"html.parser")

                carideger = parser.find("div",{"id":"ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d"})\
                .find_all("tr")


                for i in carideger:
                    bilgi1 = i.th.string
                    bilgi2 = i.td.string
                    print(f"{bilgi1} : {bilgi2}")
                break

            except AttributeError:
                print("Hatali bir sirket adi girdiniz")
                time.sleep(3)
        time.sleep(3)
        self.menudon()
    


    
    def getiri(self):
        while True:
            try:
                sirket = input("Lutfen sirket adi giriniz: ")

                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)

                parser = BeautifulSoup(requests.get(url).content,"html.parser")

                getiri = parser.find("div",{"id":"ctl00_ctl58_g_aa8fd74f_f3b0_41b2_9767_ea6f3a837982"})\
                .find("table").find("tbody").find_all("tr")

                for i in getiri:
                    bilgi = i.find_all("td")
                    print(f"""\nBirim : {bilgi[0].string} 
            Gunluk(%) : {bilgi[1].string} 
            Haftalik : {bilgi[2].string} 
            Aylik : {bilgi[3].string} 
            Yil içi getiri : {bilgi[4].string}""")

                break

            except AttributeError:
                print("Hatali bir sirket adi girdiniz")
                time.sleep(3)
        time.sleep(3)
        self.menudon()




    def dahilendeks(self):
        while True:
            try:
                sirket = input("Lutfen sirket adi giriniz: ")

                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)

                parser = BeautifulSoup(requests.get(url).content,"html.parser")

                dahiliendeks = parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"})\
                .find("table").find("tbody").find("tr")

                dahiliendeks2 = parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"})\
                .find("table").find("thead").find("tr")

                for  i in range(0,3):
                    bilgi = dahiliendeks2.find_all("th")
                    bilgi2 = dahiliendeks.find_all("td")
                    print(f"{bilgi[i].string} : {bilgi2[i].string}")


                break

            except AttributeError:
                print("Hatali bir sirket adi girdiniz")
                time.sleep(3)
        time.sleep(3)
        self.menudon()


    
    def cikis(self):
        self.dongu== False
        exit()
    


    def menudon(self):
        while True:
            x=input("\nAna menuye donmek icin 7'ye cikmak için 6'ya basiniz:\n")
            if x=="7":
                print("Ana menuye donuluyor...")
                time.sleep(3)
                self.program()
                break
                
            elif x=="6":
                self.cikis()
                break
            else:
                print("Lutfen gecerli bir secim yapiniz.")




Sistem=Hisse()
while Sistem.dongu:
    Sistem.program()














