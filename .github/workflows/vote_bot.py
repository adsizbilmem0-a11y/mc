import pyautogui
import time
import os
import sys
import random

# Terminal cikis ayari
sys.stdout.reconfigure(encoding='utf-8')

m_id = sys.argv[1] if len(sys.argv) > 1 else "1"
# Yeni oyun adını buraya tanımladık
USER_NAME = "ZdzqcvDM7o" 
CONF = 0.7 

def insansi_bekle(min_sn=2, max_sn=5):
    sure = random.uniform(min_sn, max_sn)
    time.sleep(sure)

def insansi_hareket_ve_tikla(resim, aciklama):
    print(f"[>] Araniyor: {aciklama}...")
    try:
        konum = pyautogui.locateOnScreen(resim, confidence=CONF)
        if konum:
            merkez = pyautogui.center(konum)
            # Fareyi yavasca hareket ettir
            pyautogui.moveTo(merkez.x, merkez.y, duration=random.uniform(1.2, 2.5), pyautogui.easeOutQuad)
            insansi_bekle(0.8, 1.5)
            pyautogui.click()
            print(f"[+] {aciklama} tiklandi.")
            return True
    except Exception as e:
        print(f"[!] Hata: {e}")
    print(f"[-] {aciklama} bulunamadi.")
    return False

def bot_baslat():
    print(f"\n=== MAKINE {m_id} HAZIR ===")
    print(f"[!] KULLANICI ADI: {USER_NAME}")
    print("[!] 120 SANIYE BEKLEME BASLADI. RDP ILE BAGLAN VE IZLE!")
    
    # Geri sayım logu (her 30 saniyede bir haber verir)
    for i in range(4):
        time.sleep(30)
        print(f"[DEBUG] Botun baslamasina {(3-i)*30} saniye kaldi...")

    print(f"--- INSANSI BOT CALISMAYA BASLADI ---")
    
    # 1. Isim Yazma
    if insansi_hareket_ve_tikla('username_box.png', 'Username Kutusu'):
        insansi_bekle(1.5, 3)
        # Harf harf yavasca yaz (insan gibi)
        for harf in USER_NAME:
            pyautogui.write(harf)
            time.sleep(random.uniform(0.15, 0.4))
        print(f"[+] Isim basariyla yazildi.")

    # 2. Privacy
    insansi_bekle(2, 4)
    insansi_hareket_ve_tikla('privacy_check.png', 'Privacy Checkbox')

    # 3. Cloudflare
    insansi_bekle(4, 7)
    if insansi_hareket_ve_tikla('cloudflare_check.png', 'Cloudflare Kutusu'):
        print("[DEBUG] Cloudflare tiklandi. Dogrulama icin bekleniyor (20sn)...")
        time.sleep(20) # Cloudflare icin sureyi biraz daha uzattim

    # 4. Vote
    insansi_bekle(3, 6)
    if insansi_hareket_ve_tikla('vote_btn.png', 'VOTE BUTONU'):
        print("[!!!] ISLEM TAMAMLANDI! OY VERILDI.")

if __name__ == "__main__":
    bot_baslat()
