import pyautogui
import time
import os
import sys
import random

# Terminal cikis ayari
sys.stdout.reconfigure(encoding='utf-8')

m_id = sys.argv[1] if len(sys.argv) > 1 else "1"
USER_NAME = "ZdzqcvDM7o" 
CONF = 0.7 

def insansi_bekle(min_sn=2, max_sn=5):
    time.sleep(random.uniform(min_sn, max_sn))

def insansi_hareket_ve_tikla(resim, aciklama):
    print(f"[>] Araniyor: {aciklama}...")
    try:
        konum = pyautogui.locateOnScreen(resim, confidence=CONF)
        if konum:
            merkez = pyautogui.center(konum)
            # Fareyi kavisli ve yavas hareket ettir
            pyautogui.moveTo(merkez.x, merkez.y, 
                             duration=random.uniform(1.2, 2.5), 
                             tween=pyautogui.easeOutQuad)
            insansi_bekle(0.8, 1.5)
            pyautogui.click()
            print(f"[+] {aciklama} tiklandi.")
            return True
    except Exception as e:
        print(f"[!] {aciklama} sirasinda hata: {e}")
    return False

def bot_baslat():
    print(f"\n=== MAKINE {m_id} BASLATILIYOR ===")
    print(f"[!] HEDEF OYUNCU: {USER_NAME}")
    print("[!] 120 SANIYE BEKLEME SURESI... RDP ILE GIRIS YAPIN!")
    
    for i in range(4):
        time.sleep(30)
        print(f"[DEBUG] Kalan sure: {(3-i)*30} saniye...")

    print(f"--- OTOMASYON ISLEMLERI BASLADI ---")
    
    # 1. Isim Yazma
    if insansi_hareket_ve_tikla('username_box.png', 'Username Kutusu'):
        insansi_bekle(1.5, 3)
        for harf in USER_NAME:
            pyautogui.write(harf)
            time.sleep(random.uniform(0.15, 0.4))
        print(f"[+] Isim yazma islemi bitti.")

    # 2. Privacy Check
    insansi_bekle(2, 4)
    insansi_hareket_ve_tikla('privacy_check.png', 'Privacy Checkbox')

    # 3. Cloudflare Onayi
    insansi_bekle(4, 7)
    if insansi_hareket_ve_tikla('cloudflare_check.png', 'Cloudflare Kutusu'):
        print("[DEBUG] Cloudflare onay bekliyor (20sn)...")
        time.sleep(20)

    # 4. Final Vote Butonu
    insansi_bekle(3, 6)
    if insansi_hareket_ve_tikla('vote_btn.png', 'VOTE BUTONU'):
        print("[!!!] TEBRIKLER! OY VERME TAMAMLANDI.")

if __name__ == "__main__":
    bot_baslat()
