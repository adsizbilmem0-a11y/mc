import pyautogui
import time
import os
import sys

# Terminalin Turkce karakterlerle kafayi yememesi icin cikis kodlamasini zorla
sys.stdout.reconfigure(encoding='utf-8')

# Ayarlar
CONFIDENCE = 0.8  

def click_image(image_name, message):
    print(f"[>] Searching for: {message}")
    try:
        # Resim workflows klasorunde oldugu icin direkt adıyla arıyoruz
        konum = pyautogui.locateOnScreen(image_name, confidence=CONFIDENCE)
        if konum:
            pyautogui.click(konum)
            print(f"[+] Clicked: {message}")
            return True
    except Exception as e:
        print(f"[-] Error or not found ({message}): {e}")
    return False

def start_bot():
    print("--- VOTE BOT STARTED (1440x900) ---")
    time.sleep(15)  # Chrome'un yuklenmesi icin bekleme
    
    # 1. Username kutusu
    if click_image('username_box.png', 'Username Box'):
        time.sleep(1)
        pyautogui.write("KullaniciAdin", interval=0.1) 
    
    # 2. Privacy Checkbox
    time.sleep(1)
    click_image('privacy_check.png', 'Privacy Checkbox')
    
    # 3. Cloudflare Verify
    time.sleep(1)
    click_image('cloudflare_check.png', 'Cloudflare Verify')
    
    # Bekleme (Dogrulama icin)
    time.sleep(5)
    
    # 4. Vote Button
    click_image('vote_btn.png', 'Vote Button')
    
    print("[!] Process Finished.")

if __name__ == "__main__":
    start_bot()
