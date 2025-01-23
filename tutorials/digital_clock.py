import time
from datetime import datetime
def wyswietl_czas():
    ## wyświelta aktualny czas w formacie cyfrowym
    while True:
        teraz = datetime.now()
        print("\033[H\033[J", end="")
        print("=" * 50)
        print("super zegar cyfrowy w Pythonie")
        print("=" * 50)d}:{teraz.second:     }")
        print(f"{teraz.day:02d}.{teraz.month:02d}.{teraz.year}")
        