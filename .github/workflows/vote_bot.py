import pyautogui
import time
import sys
import random

# Ekrani 1440x900 varsayiyoruz (YAML'da oyle ayarladik)
# BU DEGERLERI RDP ILE GIRIP KONTROL ETTIKTEN SONRA GUNCELLE
KOORDINATLAR = {
    "username_kutusu": (720, 450),  # Ornek: Ekranin ortasi
    "privacy_check": (600, 550),
    "cloudflare_box": (720, 650),
    "vote_butonu": (720, 800)
}

USERNAME = "ZdzqcvDM7o"

def insansi_tikla(x, y):
    # Hafif sapma payi ekle ki robot oldugu anlasilmasin (+- 3 piksel)
    hedef_x = x + random.randint(-3, 3)
    hedef_y = y + random.randint(-3, 3)
    
    pyautogui.moveTo(hedef_x, hedef_y, duration=random.uniform(0.8, 1.5), tween=pyautogui.easeOutQuad)
    time.sleep(random.uniform(0.5, 1.0))
    pyautogui.click()

def baslat():
    print("--- KONUM BULUCU MODU ---")
    print("Fareyi 10 saniye icinde tiklanacak yere getir...")
    time.sleep(10)
    print(f"SU ANKI FARE KONUMUN: {pyautogui.position()}") 
    print("-------------------------")

    print("120 saniye bekletiliyor (RDP baglantisi icin)...")
    time.sleep(120)

    # 1. Isim Yazma
    x, y = KOORDINATLAR["username_kutusu"]
    insansi_tikla(x, y)
    for harf in USERNAME:
        pyautogui.write(harf)
        time.sleep(random.uniform(0.1, 0.3))

    # 2. Privacy
    time.sleep(2)
    x, y = KOORDINATLAR["privacy_check"]
    insansi_tikla(x, y)

    # 3. Cloudflare
    time.sleep(5)
    x, y = KOORDINATLAR["cloudflare_box"]
    insansi_tikla(x, y)
    time.sleep(20) # Onaylanmasini bekle

    # 4. Vote
    x, y = KOORDINATLAR["vote_butonu"]
    insansi_tikla(x, y)
    print("ISLEM BITTI!")

if __name__ == "__main__":
    baslat()
