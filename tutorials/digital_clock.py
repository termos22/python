import time
from datetime import datetime
def wyswietl_czas():
    ## wyświelta aktualny czas w formacie cyfrowym
    while True:
        teraz = datetime.now()
        print("\033[H\033[J", end="")
        print("=" * 50)
        print("super zegar cyfrowy w Pythonie")
        print("=" * 50),{teraz.second}")
        print(f"{teraz.day:02d}.{teraz.month:02d}.{teraz.year}")
        print("\n" + "=" * 50)
        print("zegar stworzony w kilku linijkach kodu")
        print("=" * 50)
        time.sleep(1)

def main():
    try:
        wyswietl_czas()
    except KeyboardInterrupt:
        print("\n\n dziękujemy za skorzystanie z zegara")
if __name__ == "__main__":
    main()
