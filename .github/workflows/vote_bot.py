import pyautogui
import time
import os
import sys

# Terminal cikisini UTF-8 yap (Turkce karakter hatasi almamak icin)
sys.stdout.reconfigure(encoding='utf-8')

# Makine numarasini al
m_id = sys.argv[1] if len(sys.argv) > 1 else "X"
USER_NAME = f"Mert_Gamer_{m_id}" # Burayi istersen sabit bir isim yapabilirsin
CONF = 0.7 # Benzerlik orani (%70)

def debug_ekran_kaydet(hata_adi):
    if not os.path.exists("debug_screenshots"):
        os.makedirs("debug_screenshots")
    pyautogui.screenshot(f"debug_screenshots/hata_{hata_adi}.png")
    print(f"[DEBUG] Ekran goruntusu alindi: hata_{hata_adi}.png")

def akilli_tikla(resim, aciklama, bekle=2):
    print(f"[>] Araniyor: {aciklama} ({resim})...")
    try:
        # Resim dosyasinin varligini kontrol et
        if not os.path.exists(resim):
            print(f"[!] HATA: {resim} dosyasi klasorde bulunamadi!")
            return False

        # Ekranda ara
        konum = pyautogui.locateOnScreen(resim, confidence=CONF)
        
        if konum:
            merkez = pyautogui.center(konum)
            pyautogui.click(merkez)
            print(f"[+] BASARILI: {aciklama} tiklandi. Koordinat: {merkez}")
            time.sleep(bekle)
            return True
        else:
            print(f"[-] UYARI: {aciklama} ekranda bulunamadi.")
            return False
    except Exception as e:
        print(f"[!] KRITIK HATA ({aciklama}): {e}")
        debug_ekran_kaydet(aciklama.replace(" ", "_"))
        return False

def bot_baslat():
    print(f"\n--- BOT CALISIYOR | MAKINE: {m_id} | USER: {USER_NAME} ---")
    
    # 1. Username Kutusu
    if akilli_tikla('username_box.png', 'Username Kutusu'):
        pyautogui.write(USER_NAME, interval=0.1)
        print(f"[+] Isim yazildi: {USER_NAME}")
    else:
        # Eger bulamazsa sayfayi biraz asagi kaydirip tekrar dene
        print("[DEBUG] Kutusu bulunamadı, sayfa kaydiriliyor...")
        pyautogui.scroll(-300)
        akilli_tikla('username_box.png', 'Username Kutusu (Tekrar)')

    # 2. Privacy Checkbox
    akilli_tikla('privacy_check.png', 'Privacy Checkbox')

    # 3. Cloudflare Onayi
    if akilli_tikla('cloudflare_check.png', 'Cloudflare Kutusu', bekle=8):
        print("[DEBUG] Cloudflare tiklandi, onay bekleniyor...")
    
    # 4. Vote Butonu
    if akilli_tikla('vote_btn.png', 'VOTE BUTONU'):
        print("[!!!] ISLEM TAMAMLANDI! OY VERILDI.")
    else:
        print("[!] Vote butonu bulunamadigi icin islem bitirilemedi.")
        debug_ekran_kaydet("vote_butonu_yok")

if __name__ == "__main__":
    bot_baslat()
