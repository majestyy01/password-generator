import tkinter as tk
import random
import string
"""
WoxicDEV - 2024 
Instagram - mertt.js_
LinkedIn : Mert Ali Kaya
chiefdelphi : mrtalikyaa
Tek tek uğraşmaktansa direk string kütüphanesini kullandım.
Readme file da kütüphanenin detaylarını paylaştım.
"""
def sifre_uret():
  zorluk = secilen_zorluk_radiobutton.get()
  uzunluk = int(uzunluk_girisi.get())

  if zorluk == "1":
    # Küçük harfler ve sayılar
    karakterler = string.ascii_lowercase + string.digits
  elif zorluk == "2":
    # Büyük ve küçük harfler, sayılar
    karakterler = string.ascii_letters + string.digits
  else:
    # Tüm karakterler
    karakterler = string.ascii_letters + string.digits + string.punctuation
    #burada belirttiğimiz uzunluğa göre şifreyi ayarlıyor ve üretiyor
  sifre = "".join(random.choice(karakterler) for _ in range(uzunluk))
  sifre_label.config(text=f"Rastgele Şifreniz: {sifre}")

def kopyala():
    #panoya kopyalama kısmı
  sifre = sifre_label.cget("text")[18:] # "Rastgele Şifreniz: " kısmını kopyalamaz
  panoya_kopyala(sifre)

def panoya_kopyala(sifre):
    #panoya metin kopyalama bölümü
  root = tk.Tk()
  root.withdraw()
  root.clipboard_clear()
  root.clipboard_append(sifre)
  root.update()
  root.destroy()

# Pencereyi oluşturma
pencere = tk.Tk()
pencere.title("Password Generator by WoxicDEV")
pencere.geometry("400x400") # Pencere boyutlarını ayarlama ben 400x400 yaptım büyütürseniz tavsiyem içerikleride büyütün.

#Pencerenin arkaplan rengini ayarlama
pencere.config(bg="#F0F0F0") # Açık gri arka plan rengi

# Zorluk Seviyesi ayarlama bölümleri
zorluk_frame = tk.Frame(pencere, bg="#E0E0E0", relief=tk.RAISED, bd=2) # Zorluk çerçevesi
zorluk_frame.pack(padx=20, pady=20)

zorluk_label = tk.Label(zorluk_frame, text="Zorluk Seviyesi:", font=("Arial", 12, "bold"), bg="#E0E0E0")
zorluk_label.grid(row=0, column=0, padx=5, pady=5)
#zorluk bölümünde olan radio buttonlar
secilen_zorluk_radiobutton = tk.StringVar()
zorluk_1_radiobutton = tk.Radiobutton(zorluk_frame, text="Kolay", variable=secilen_zorluk_radiobutton, value="1", font=("Arial", 10), bg="#E0E0E0")
zorluk_1_radiobutton.grid(row=1, column=0, padx=5, pady=5)
zorluk_2_radiobutton = tk.Radiobutton(zorluk_frame, text="Orta", variable=secilen_zorluk_radiobutton, value="2", font=("Arial", 10), bg="#E0E0E0")
zorluk_2_radiobutton.grid(row=2, column=0, padx=5, pady=5)
zorluk_3_radiobutton = tk.Radiobutton(zorluk_frame, text="Zor", variable=secilen_zorluk_radiobutton, value="3", font=("Arial", 10), bg="#E0E0E0")
zorluk_3_radiobutton.grid(row=3, column=0, padx=5, pady=5)

# Şifre Uzunluğu ayarlama kısmı
uzunluk_frame = tk.Frame(pencere, bg="#E0E0E0", relief=tk.RAISED, bd=2) # Uzunluk çerçevesi
uzunluk_frame.pack(padx=20, pady=20)

uzunluk_label = tk.Label(uzunluk_frame, text="Şifre Uzunluğu:", font=("Arial", 12, "bold"), bg="#E0E0E0")
uzunluk_label.grid(row=0, column=0, padx=5, pady=5)

uzunluk_girisi = tk.Entry(uzunluk_frame, width=5, font=("Arial", 10), bg="#FFFFFF")
uzunluk_girisi.grid(row=0, column=1, padx=5, pady=5)

# Şifre Üreten Buton
sifre_uret_butonu = tk.Button(pencere, text="Şifre Üret", command=sifre_uret, font=("Arial", 12, "bold"), bg="#CCCCCC")
sifre_uret_butonu.pack(pady=20, anchor=tk.CENTER)

# Şifreyi Yazdıran buton
sifre_label = tk.Label(pencere, text="Rastgele Şifreniz:", font=("Arial", 12, "bold"))
sifre_label.pack()

# Kopyalama Butonu (metin olarak ekranda belirtilmesede sorunsuz kopyalıyor.)
kopyalama_butonu = tk.Button(pencere, text="Kopyala", command=kopyala, font=("Arial", 10), bg="#CCCCCC")
kopyalama_butonu.pack(pady=10, anchor=tk.CENTER)


pencere.mainloop()
