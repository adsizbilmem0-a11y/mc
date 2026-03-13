import pyautogui
import time
import sys
import random

# Makine ID'sini al
m_id = sys.argv[1] if len(sys.argv) > 1 else "1"
USERNAME = "ZdzqcvDM7o"

# BU KOORDINATLARI RDP ILE GIRINCE LOGLARDAN BAKIP GUNCELLE
KOORDINATLAR = {
    "username": (650, 480),
    "privacy": (420, 560),
    "cloudflare": (550, 680),
    "vote_btn": (650, 820)
}

def baslat():
    print(f"--- MAKINE {m_id} BASLADI ---")
    
    # RDP ile girdiginde koordinat bulmana yardimci olur
    for i in range(15):
        print(f"Fare Konumu (Logda gorunur): {pyautogui.position()}")
        time.sleep(1)

    print("120 saniye bekleniyor... RDP ile siteye odaklanın.")
    time.sleep(120)

    try:
        # 1. Username Kutusu
        x, y = KOORDINATLAR["username"]
        pyautogui.click(x, y, duration=1.0)
        time.sleep(1)
        pyautogui.write(USERNAME, interval=0.2)

        # 2. Privacy
        x, y = KOORDINATLAR["privacy"]
        pyautogui.click(x, y, duration=1.0)
        time.sleep(2)

        # 3. Cloudflare
        x, y = KOORDINATLAR["cloudflare"]
        pyautogui.click(x, y, duration=1.0)
        print("Cloudflare onay bekleniyor (20sn)...")
        time.sleep(20)

        # 4. Vote Butonu
        x, y = KOORDINATLAR["vote_btn"]
        pyautogui.click(x, y, duration=1.0)
        print("Bitti!")
        
    except Exception as e:
        print(f"Hata olustu: {e}")

if __name__ == "__main__":
    baslat()
