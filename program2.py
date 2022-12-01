from collections import defaultdict, namedtuple

class Podsumowanie_zamownien:
    def __init__(self):
        self._klientki = defaultdict(Zakupy)

    def klient(self, name):
        return self._klientki[name]
        

Order = namedtuple('Order', ('amount', 'price'))

class Zakupy:
    def __init__(self):
        self._zamowienia = []

    def raport_zamowienia(self, amount, price):
        self._zamowienia.append(Order(amount, price))

    def srednio_wydane(self):
        total, counter = 0,0
        for zamownienie in self._zamowienia:
            total += zamownienie.amount * zamownienie.price
            counter += 1
        return total/counter

class Klientka:
    def __init__(self):
        self._zakupy = {}

    def dodaj_klienta(self, name):
        self._zakupy[name] = []

    def get_zakupy(self, name, price):
        self._zakupy[name].append(price)

    def wydane_pieniadze(self, name):
        wydatki = self._zakupy[name]
        return sum(wydatki)
    

book = Podsumowanie_zamownien()

anna = book.klient('Anna Nowak')
anna.raport_zamowienia(4, 140)
anna.raport_zamowienia(1, 100)
anna.raport_zamowienia(2, 200)

print(f'Podczas jednego zamówienia Anna średnio wydaje:', anna.srednio_wydane())

klient = Klientka()
klient.dodaj_klienta('Barbara Kowalska')
klient.get_zakupy('Barbara Kowalska', 100)
klient.get_zakupy('Barbara Kowalska', 130)
klient.get_zakupy('Barbara Kowalska', 330)
print('Barbara wydała w tym sklepie:', klient.wydane_pieniadze('Barbara Kowalska'))


