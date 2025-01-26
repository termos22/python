# Zegar cyfrowy - prosty program pokazujący moc Pythona!
# Autor: Tukano Software House
# Data: 2024
# źródło: https://github.com/tukanosoftwarehouse/python-ai-edu/blob/master/stage_01/03/03_2_zegar_cyfrowy.py

import time
from datetime import datetime
def wyswietl_czas():
    # wyświelta aktualny czas w formacie cyfrowym
    while True:
        teraz = datetime.now() # pobierz aktualny czas
        print("\033[H\033[J", end="") # wyczyść ekran działa na większości systemów
        
        # wyświetla ozdobny baner
        print("=" * 50)
        print("⌚ super zegar cyfrowy w Pythonie")
        print("=" * 50)

        # wyświetla czas i datę
        print(f"\n{teraz.hour:02d}:{teraz.minute:02d}:{teraz.second:02d}")
        print(f"📅{teraz.day:02d}.{teraz.month:02d}.{teraz.year}")
        
        # Ozdobny separator
        print("\n" + "=" * 50)
        print("🚀 zegar stworzony w kilku linijkach kodu")
        print("=" * 50)
        
        time.sleep(1) # czekaj sekunę przed kolejnym odświeżeniem

def main():
    try:
        wyswietl_czas()
    except KeyboardInterrupt:
        print("\n\n dziękujemy za skorzystanie z zegara")


if __name__ == "__main__":
    main()
