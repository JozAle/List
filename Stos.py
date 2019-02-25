class Stos:  # Klasza kolejki priorytetowej na Stosie Max
    def __init__(self):  # Tworzenie obiektu klasy Stos
        self.items = []  # Utworzenie pustej listy pythona

    def __str__(self):  # Stworzenie metody print()
        return str(self.items)  # Zwraca elementy listy jako string

    def isEmpty(self):  # Funkcja sprawdzajaca czy obiekt jest pusty
        if self.items == []:  # Jesli na liscie nie ma elementow
            print('Lista jest pusta.')  # Wypisuje komunikat
            return 1  # Zwraca wartosc True
        else:  # Jesli nie jest pusta
            print('Lista nie jest pusta.')  # Wypisuje komunikat
            return 0  # Zwraca wartosc False

    def push(self, item):  # Funkcja dodajaca element do stosu
        self.items.append(item)  # Dodanie item na koniec stosu
        self.ustaw()  # Uzycie funkcji sortowanie

    def ustaw(self):  # Funkcja sortujaca
        self.items.sort()  # Sortowanie elementow stosu

    def peek(self):  # Funkcja zwracajaca element na szczycie stosu
        return self.items[self.size() - 1]  # Zwracanie elementu na ostatnim indeksie

    def size(self):  # Funkcja zwracajaca rozmiar obietu
        return len(self.items)  # Zwraca dlugosc listy

    def pop(self):  # Usuniecie najwiekszego elementu
        return self.items.pop()  # Zwraca ostatni element z list i go usuwa

if __name__ == '__main__':
    Stos = Stos()
    Stos.push(5)
    Stos.push(2)
    Stos.push(8)
    print(Stos)
    Stos.pop()
    Stos.push(6)
    print(Stos)
    Stos.pop()
    print(Stos.peek())
    print(Stos)
