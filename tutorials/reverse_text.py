def odwroc_slowo(tekst):
    ### odwraca kolejność liter w tekście 
    return tekst[::-1]

def main():
    print("=" * 50)
    print("Witaj w magicznym odwracaczu słów")
    print("Zamień dowolny tekst w jego lustrzane odbicie")
    print("=" * 50)
    try:
        tekst = input("\n Wpisz dowolny tekst: ")
        odwrocony = odwroc_slowo(tekst)
        print("\n" + "<" * 10)
        print(f"Oryginalny teks: {tekst}")
        print(f"Odwrócony tekst: {odwrocony}")
        print("<" * 10)
    except KeyboardInterrupt:
        print("\n\n Przerwano działanie programu.")
    print("\n Dziękujemy za skorzystanie z programu")
if __name__ == "__main__":
    main()