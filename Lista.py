class Queue:  # Klasa Kolejki Priorytetowej na liscie Pythona
    def __init__(self):  # Tworzenie obiektu klasy Queue
        self.items = []  # Na pustej liscie pythona

    def __str__(self):  # Definicja metody print()
        return "Lista priorytetowa: " + str(self.items)  # Zwraca elementy obiektu Queue jako string

    def isEmpty(self):  # Funkcja sprawdzajaca czy obiekt klasy Queue jest pusty
        if self.items == []:  # Jesli na liscie nie ma elementow
            print('Lista jest pusta.')  # Wypisuje komunikat
            return 1  # Zwraca wartosc True
        else:  # Jesli nie jest pusta
            print('Lista nie jest pusta.')  # Wypisuje komunikat
            return 0  # Zwraca wartosc False

    def enqueue(self, item):  # Funkcja dodajaca item.
        self.items.insert(0, item)  # Dodawanie item na poczatek kolejki

    def dequeue(self):  # Funkcja usuwajaca najwiekszy element z kolejki
        self.items.remove(max(self.items))  # Usuwanie najwiekszego elementu

    def size(self):  # Funkcja zwracajaca ilosc elementow w obiekcie klasy Queue
        return len(self.items)  # Zwraca dlugosc obiektu



if __name__ == '__main__':
    Kolejka = Queue()
    Kolejka.isEmpty()
    Kolejka.enqueue(2)
    Kolejka.enqueue(4)
    Kolejka.dequeue()
    print(Kolejka)
    Kolejka.enqueue(3)
    Kolejka.enqueue(4)
    Kolejka.enqueue(2)
    Kolejka.enqueue(2)
    print(Kolejka)
    Kolejka.dequeue()
    print(Kolejka)
    Kolejka.isEmpty()
