'''Dobieranie rozmiaru'''

def typ_sukienki(wymiar, dlugosc = 25):
    '''Funkcja zwaraca informacje o typie sukienki dla danej klientki
    dlugosc - calkowita dlugosc spodnicy
    wymiar - zmierzona długość od biodra do kostki'''
    try:
        if dlugosc<(wymiar/4):
            print("Ta spódnica będzie Ciebie będzie typu: MINI")
            return 1
        if dlugosc<(wymiar/2):
            print("Ta spódnica będzie Ciebie będzie typu: MIDI")
            return 2
        else:
            print("Ta spódnica będzie Ciebie będzie typu: MAXI")
            return 3
    except ValueError:
        print("Podane wymiary są błędne")
        return 0

def sortowanie(klientki):
    def helper(x):
        if (lambda x: x<(25/4))==1:
            return (1,x)
        return(2,x)
    klientki.sort(key=helper)

args = {120,60}        
typ_sukienki(*args)

klientki = [120, 110, 100, 90, 115]
'''Informacja zawrotna dla całej listy klientek:'''
result = list(map(typ_sukienki, klientki))
print(f"Wynik map: {result}")

'''Jakiego typu jest nasz produkt dla klientek?'''
mini = filter(lambda rozmiar: rozmiar == 1, result)
print(f'Dla {len(list(mini))} klientek sukienka ma długość mini')
midi = filter(lambda rozmiar: rozmiar == 2, result)
print(f'Dla {len(list(midi))} klientek sukienka ma długość midi')
maxi = filter(lambda rozmiar: rozmiar == 3, result)
print(f'Dla {len(list(maxi))} klientek sukienka ma długość maxi')

print(f'lista klientek przed sortowaniem {klientki}')
sortowanie(klientki)
print(f'klientki posortowane według klucza mini: {klientki}')


