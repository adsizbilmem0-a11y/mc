import pyautogui
import time
import os

# Ayarlar
CONFIDENCE = 0.8  # Resim eşleşme hassasiyeti

def tıkla(resim_adı, mesaj):
    print(f"[>] {mesaj} aranıyor...")
    try:
        # Resim ana dizinde olduğu için direkt adıyla arıyoruz
        konum = pyautogui.locateOnScreen(resim_adı, confidence=CONFIDENCE)
        if konum:
            pyautogui.click(konum)
            print(f"[+] {mesaj} tıklandı!")
            return True
    except Exception as e:
        print(f"[-] {mesaj} bulunamadı veya hata oluştu.")
    return False

def baslat():
    print("--- VOTE BOTU BASLATILDI (1440x900) ---")
    time.sleep(15)  # Chrome'un yüklenmesi için süre
    
    # 1. Username kutusuna tıkla ve yaz
    if tıkla('username_box.png', 'Kullanıcı adı kutusu'):
        time.sleep(1)
        pyautogui.write("KullaniciAdin", interval=0.1) # Burayı değiştirirsin
    
    # 2. Privacy Checkbox
    time.sleep(1)
    tıkla('privacy_check.png', 'Gizlilik kutucuğu')
    
    # 3. Cloudflare Verify
    time.sleep(1)
    tıkla('cloudflare_check.png', 'Cloudflare doğrulaması')
    
    # Cloudflare sonrası biraz bekle (doğrulanması için)
    time.sleep(5)
    
    # 4. Vote Butonu
    tıkla('vote_btn.png', 'Vote butonu')
    
    print("[!] İşlem bitti.")

if __name__ == "__main__":
    baslat()
