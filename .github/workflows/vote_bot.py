import pyautogui
import time
import sys
import random
import os

pyautogui.FAILSAFE = False

MACHINE_ID = sys.argv[1] if len(sys.argv) > 1 else "1"

USERNAME = "ZdzqcvDM7o"

CONFIDENCE = 0.7

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def img(name):
    return os.path.join(BASE_DIR, name)


def human_wait(a=2,b=5):
    time.sleep(random.uniform(a,b))


def find_and_click(image,desc):

    print(f"[>] Araniyor: {desc}")

    try:

        pos = pyautogui.locateOnScreen(
            img(image),
            confidence=CONFIDENCE,
            grayscale=True,
            region=(0,0,1440,900)
        )

        if pos:

            center = pyautogui.center(pos)

            pyautogui.moveTo(
                center.x,
                center.y,
                duration=random.uniform(1.2,2.3),
                tween=pyautogui.easeOutQuad
            )

            human_wait(0.5,1.2)

            pyautogui.click()

            print(f"[+] {desc} tiklandi")

            return True

    except Exception as e:
        print(f"Hata: {e}")

    return False


def wait_and_click(image,desc,timeout=60):

    start = time.time()

    while time.time() - start < timeout:

        if find_and_click(image,desc):
            return True

        time.sleep(2)

    print(f"[X] {desc} bulunamadi")

    return False


def type_username():

    human_wait()

    for letter in USERNAME:

        pyautogui.press(letter)

        time.sleep(random.uniform(0.15,0.35))


def start_bot():

    print("\n====================")
    print(f"MAKINE {MACHINE_ID}")
    print("====================\n")

    print("120 saniye bekleniyor (RDP baglanmak icin)")
    time.sleep(120)

    print("BOT BASLADI")

    if wait_and_click("username_box.png","username kutusu"):
        type_username()

    human_wait()

    wait_and_click("privacy_check.png","privacy checkbox")

    human_wait()

    if wait_and_click("cloudflare_check.png","cloudflare"):
        time.sleep(20)

    human_wait()

    wait_and_click("vote_btn.png","vote butonu")

    print("ISLEM TAMAMLANDI")


if __name__ == "__main__":
    start_bot()
