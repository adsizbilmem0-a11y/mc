import pyautogui
import time
import sys
import os

def koordinat_avcisi():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    dosya_yolu = os.path.join(desktop, "KOORDINAT_NOTLARI.txt")
    
    print("Koordinat avcisi basladi! 20 saniye boyunca fareyi kutularin uzerinde tut.")
    
    with open(dosya_yolu, "w") as f:
        f.write("=== KOORDINAT LISTESI ===\n")
        for i in range(20):
            pos = pyautogui.position()
            satir = f"Saniye {i+1}: X={pos.x}, Y={pos.y}\n"
            f.write(satir)
            # Terminale de bas (Eger gorebilirsen)
            print(satir.strip())
            time.sleep(1)
            
    print(f"Koordinatlar masaustune kaydedildi: {dosya_yolu}")

if __name__ == "__main__":
    koordinat_avcisi()
