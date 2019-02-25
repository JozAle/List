class Node:  # Klasa Node obslugujaca wezly listy z dowiazaniami
    def __init__(self, initdata):  # Tworzenie obiektu klasy Node
        self.data = initdata  # z Dana initdata
        self.next = None  # Oraz adresem nastepnego rownym None


    def getData(self):  # Funkcja zwracajaca wartosc Node
        return self.data


    def getNext(self):  # Funkcja zwracajaca adres do nastepnego Node
        return self.next


    def setData(self, newdata):  # Funkcja zmieniajaca wartosc Node
        self.data = newdata


    def setNext(self, newnext):  # Funkcja ustwiajaca inny Node jako nastepny
        self.next = newnext


class OrderedList:  # Klasa obiektu listy z dowiazaniami, uporzadkowana.
    def __init__(self):  # Tworzenie obiektu klasy
        self.head = None  # Na poczatku head = None poniewaz nie ma zadnych Node


    def __str__(self):  # Zmiana metody print() po to by moc wyswietlac obiekty klasy OderedList
        Elementy = []  # Stworzenie pustej listy
        Element = self.head  # Ustalenie pierwszego elementu
        while(Element != None):  # Dopoki nie dotre do ostatniego elementu rownego None
            Elementy.append(Element.getData())  # Dopisywanie do listy wartosci wezlow
            Element = Element.getNext()  # Przejscie na kolejny wezel
        return str(Elementy)  # Zwrocenie tabelki jako string


    def isEmpty(self):  # Funkcja sprawdzajaca czy obiekt jest pusty
        return self.head == None  # Jesli head jest rowny None oznacza ze nie ma zadnych wezlow czyli jest pusty


    def add(self, item):  # Funkcja dodajaca wezel z item do listy
        Element = self.head  # Ustalenie pierwszego elementu
        Ostatni = None  # ustalenie elementu ostatnio mijanego czyli poprzedniego
        while Element != None:  # Przejscie po wszystkich wezlach listy
            if Element.getData() < item:  # Jesli wartosc w obecnym wezle jest mniejsza od wstawianego item
                break  # Konczy petle by obecny byl odpowiedni wezel
            else:  # Jesli nie
                Ostatni = Element # To wartosc poprzedniego jest rowna obecnemu
                Element = Element.getNext()  # A obecny elemeny przyjmuje nastepny
        Tymczasowy = Node(item)  # Stworzenie nowego wezla ktory zostanie wstawiony
        if Ostatni == None:  # Jesli Poprzedni jest rowny None czyli obecny element to poczatek listy
            Tymczasowy.setNext(self.head)
            self.head = Tymczasowy  # Tymczasowy zostaje wstawiony przed head i staje sie nowym head
        else:  # Jesli nie
            Tymczasowy.setNext(Element)
            Ostatni.setNext(Tymczasowy)  # Tymczasowy zostaje wepchniety miedzy wartosc mniejsza i wieksza


    def size(self):  # Funkcja sprawdzajaca ilosc elementow w obiekcie
        Element = self.head  # Ustwienie pierwszego elementu
        count = 0  # Ustawienie licznika
        while Element != None:  # petla iterujaca po wszystkich wezlach
            count = count + 1  # Zwiekszenie licznika
            Element = Element.getNext()  # Przejscie na kolejny element

        return count  # Zwraca wartosc licznika


    def search(self, item):  # Funkcja sprawdzajaca czy jest item na liscie oraz na jakim miejscu
        Indeks = 0  # Ustalenie poczatkowej wartosci indeksu
        Znalezione = False  # Ustawienie poczatkowej wartosci Znalezione
        Element = self.head  # Ustawienie wezla poczatkowego
        if Element.getData() == item:  # Jesli wartosc wezla jest rowna item
            Znalezione = True  # Zmiana Znalezione na True
        else:  # Jesli nie
            while(Element != None):  # Petla iterujaca po wszystkich wezlach
                if Element.getData() == item:  # Jesli wartosc wezla jest rowna item
                    Znalezione = True  #  Zmiana Znalezione na True
                    return Indeks, Znalezione  # Zwraca wartosc Indeks oraz Czy jest Znalezione
                Element = Element.getNext()  # Przejscie na kolejny element
                Indeks += 1  # Zwiekszenie indeks o 1
        return Indeks, Znalezione  # Zwraca wartosc Indeks oraz Czy jest Znalezione


    def remove(self):  # Usuniecie najwiekszego elementu z listy
        self.head = self.head.getNext()  # Usuniecie poprzez ustanowienie drugiego elementu pierwszym


if __name__ == '__main__':
    Lista = OrderedList()
    print('Czy lista jest pusta? ' + str(Lista.isEmpty()))
    Lista.add(3)
    print(Lista)
    Lista.add(4)
    print(Lista)
    Lista.add(7)
    print(Lista)
    Lista.add(1)
    print(Lista)
    Lista.add(8)
    print(Lista)
    print('Czy lista jest pusta? ' + str(Lista.isEmpty()))
    print('Rozmiar Listy: ' + str(Lista.size()))
    Liczba = 4
    Indeks, Wynik = Lista.search(Liczba)
    if Wynik == True:
        print('Liczba ' + str(Liczba) + ' znajduje sie na pozycji ' + str(Indeks))
    else:
        print('Liczba ' + str(Liczba) + ' nie znajduje sie na liscie.')
    Liczba = 9
    Indeks, Wynik = Lista.search(Liczba)
    if Wynik == True:
        print('Liczba ' + str(Liczba) + ' znajduje sie na pozycji ' + str(Indeks))
    else:
        print('Liczba ' + str(Liczba) + ' nie znajduje sie na liscie.')
    print(Lista)
    Lista.remove()
    print(Lista)
    Lista.remove()
    print(Lista)
    Lista.remove()
    print(Lista)
    Lista.remove()
    print(Lista)
    Lista.remove()
    print(Lista)

