import pyautogui
import time
import random

# Senin Paint ile bulduğun milimetrik noktalar
KOORDINATLAR = {
    "nick": (335, 558),
    "checkbox": (150, 600),
    "cloudflare": (163, 654),
    "vote_btn": (176, 716)
}

USERNAME = "ZdzqcvDM7o"

def operasyon():
    # Tunel acildiktan sonra senin baglanman icin 2 dakika bekler
    print("Bore tuneli acildi. RDP ile baglanman icin 120 saniye bekleniyor...")
    time.sleep(120) 
    
    print("--- TIKLAMA ISLEMI BASLIYOR ---")
    
    # 1. Nick Yazma
    pyautogui.click(KOORDINATLAR["nick"], duration=1.0)
    time.sleep(1)
    for harf in USERNAME:
        pyautogui.write(harf)
        time.sleep(random.uniform(0.1, 0.3))
    
    # 2. Checkbox (I agree)
    time.sleep(1.5)
    pyautogui.click(KOORDINATLAR["checkbox"], duration=0.8)
    
    # 3. Cloudflare
    time.sleep(2)
    pyautogui.click(KOORDINATLAR["cloudflare"], duration=0.8)
    print("Cloudflare onaylanmasi bekleniyor (30 saniye)...")
    time.sleep(30) # Cloudflare icin biraz daha uzun tuttum garantici olsun
    
    # 4. Vote Butonu
    pyautogui.click(KOORDINATLAR["vote_btn"], duration=1.0)
    print("Bitti! Oylama yapildi.")

if __name__ == "__main__":
    operasyon()
