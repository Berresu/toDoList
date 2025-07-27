from datetime import datetime

gorevlerList = []

def gorevEkle():
    gorev = input("Bir Görev Girin: ")

    print("Görev Önceliği Seçiniz(1(Düşük), 2(Orta), 3(Yüksek)): ")
    secim=input("Seçiminiz: ")
    if secim=="1":
      oncelik="Düşük"
    elif secim=="2":
      oncelik="Orta"
    elif secim=="3":
      oncelik="Yüksek"
    else:
      print("Geçersiz Öncelik Numarası.")

    sonTarih=input("Deadline Giriniz(GG-AA-YYYY): ")
    try:
      deadline=datetime.strptime(sonTarih, "%d-%m-%Y")
    except ValueError:
      print("Tarih Formatı Hatalı.")
      deadline=datetime.now()

    kontrol = input("Görev Tamamlandı mı? (+/-): ").strip().lower()
    if kontrol == '+':
        tamamlandi = True
    else:
        tamamlandi = False

    gorevlerList.append({"gorev": gorev, "tamamlandi": tamamlandi, "oncelik": oncelik, "deadline": deadline})
    print(f'"{gorev}" Görevi Listeye Eklendi. Öncelik Seviyesi: {oncelik}, Son Teslim Tarihi: {deadline.strftime("%d-%m-%Y")}')

def gorevListesi():
    if not gorevlerList:
        print("Görev Bulunmamaktadır.")
    else:
        print("\nGörev Listesi:")
        for i, gorev in enumerate(gorevlerList):
            durum = "+" if gorev["tamamlandi"] else "-"
            print(f"{i+1}. {gorev['gorev']} | {gorev['oncelik']} | {gorev['deadline']} | {durum}")

def gorevTamamla(index):
    if 0 <= index < len(gorevlerList):
        gorevlerList[index]["tamamlandi"] = True
        print(f'"{gorevlerList[index]["gorev"]}" görevi tamamlandı.')
    else:
        print("Geçersiz Görev Numarası.")

def gorevSil(index):
  if 0<=index<len(gorevlerList):
    sil=gorevlerList.pop(index)
    print(f"{sil['gorev']} Görevi Silindi.")
  else:
    print("Geçersiz Görev Numarası.")

def gorevDuzenle():
  gorevListesi()
  try:
    sira=int(input("Düzenlemek İstediğiniz Görevi Seçin: "))
    if 1<=sira<=len(gorevlerList):
      duzenlenenGorev=input("Yeni Görev Metnini Giriniz: ").strip()
      if duzenlenenGorev=="":
        print("Görev Metni null Olamaz.")
        return
      gorevlerList[sira-1]["gorev"]=duzenlenenGorev
      print("Görev Güncellendi.")
    else:
      print("Geçersiz Görev Numarası.")
  except ValueError:
    print("Geçersiz İşlem Numarası.")

while True:
  print("\n1- Görev Ekle")
  print("2- Görevleri Listele")
  print("3- Görev Tamamla")
  print("4- Görev Düzenle")
  print("5- Görev Sil")
  print("6- Çıkış")

  secim = input("Bir Seçenek Seçiniz (1-6): ")

  if secim=="1":
    gorevEkle()
  elif secim=="2":
    gorevListesi()
  elif secim=="3":
    gorevListesi()
    try:
      index = int(input("Tamamlanan Görevin Numarası: ")) -1
      gorevTamamla(index)
    except ValueError:
      print("Geçerli Bir Sayı Giriniz.")
  elif secim=="4":
    gorevDuzenle()
  elif secim=="5":
    try:
      index=int(input("Silmek İstediğiniz Görevin Numarası: ")) -1
      gorevSil(index)
    except ValueError:
      print("Geçerli Bir Sayı Giriniz.")
  elif secim=="6":
    print("Program Sonlandı...")
    break
  else:
    print("Geçersiz İşlem Numarası. 1-6 Arası Bir Numara Seçimi Yapınız.")
