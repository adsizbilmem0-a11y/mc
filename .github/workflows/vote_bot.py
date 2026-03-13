import pyautogui
import time
import sys
import random

m_id = sys.argv[1] if len(sys.argv) > 1 else "1"
USERNAME = "ZdzqcvDM7o"

# BURADAKI SAYILARI RDP ILE GIRINCE GORDUGUN DEGERLERLE DEGISTIR
KOORDINATLAR = {
    "username": (650, 480),
    "privacy": (420, 560),
    "cloudflare": (550, 680),
    "vote_btn": (650, 820)
}

def baslat():
    print(f"--- MAKINE {m_id} IZLENIYOR ---")
    
    # Ilk 15 saniye boyunca her saniye farenin yerini loglara basar
    # Boylece RDP icinden hangi kutunun hangi X,Y degerinde oldugunu anlarsin
    for i in range(15):
        print(f"Fareyi kutunun uzerine tut! Su anki konum: {pyautogui.position()}")
        time.sleep(1)

    print("120 saniye RDP bekleme suresi basladi...")
    time.sleep(120)

    # 1. Username
    x, y = KOORDINATLAR["username"]
    pyautogui.click(x, y, duration=1.2)
    time.sleep(1)
    pyautogui.write(USERNAME, interval=0.2)

    # 2. Privacy
    x, y = KOORDINATLAR["privacy"]
    pyautogui.click(x, y, duration=1.0)
    time.sleep(2)

    # 3. Cloudflare
    x, y = KOORDINATLAR["cloudflare"]
    pyautogui.click(x, y, duration=1.0)
    print("Cloudflare icin 20sn bekleniyor...")
    time.sleep(20)

    # 4. Vote
    x, y = KOORDINATLAR["vote_btn"]
    pyautogui.click(x, y, duration=1.2)
    print("ISLEM TAMAM!")

if __name__ == "__main__":
    baslat()
