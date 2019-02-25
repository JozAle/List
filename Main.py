from Lista import Queue
from Stos import Stos
from Wiazania import OrderedList
import random
import time
import numpy
import matplotlib.pyplot as plt

Kolejka = Queue()
Stos = Stos()
Lista = OrderedList()
CzasyKolejka = []
CzasyStos = []
CzasyLista = []

with open('CzasyKolejka.txt', 'w') as plik:
    print('Czasy dla kolejki priorytetowej na liscie pythona:', file=plik)

with open('CzasyStos.txt', 'w') as plik:
    print('Czasy dla kolejki priorytetowej na stosie:', file=plik)

with open('CzasyLista.txt', 'w') as plik:
    print('Czasy dla kolejki priorytetowej na liscie uporzadkowanej:', file=plik)

for i in range(10, 17):
    Ilosc = 2**i
    CzasKolejkaStart = time.time()
    for j in range(0, Ilosc):
        Liczba = random.randint(0, 2**20)
        Kolejka.enqueue(Liczba)
    for j in range(0, Ilosc):
        Kolejka.dequeue()
    CzasKolejkaStop = time.time()
    CzasyKolejka.append(CzasKolejkaStop - CzasKolejkaStart)

    CzasStosStart = time.time()
    for j in range(0, Ilosc):
        Liczba = random.randint(0, 2**20)
        Stos.push(Liczba)
    for j in range(0, Ilosc):
        Stos.pop()
    CzasStosStop = time.time()
    CzasyStos.append(CzasStosStop - CzasStosStart)

    CzasListaStart = time.time()
    for j in range(0, Ilosc):
        Liczba = random.randint(0, 10000)
        Lista.add(Liczba)
    for j in range(0, Ilosc):
        Lista.remove()
    CzasListaStop = time.time()
    CzasyLista.append(CzasListaStop - CzasListaStart)

with open('CzasyKolejka.txt', 'a') as plik:
    for i in range(10, 17):
        print('Czas obslugi Kolejki dla ' + str(2**i) + ' elementow: ' + '%.4f' % CzasyKolejka[i-10], file=plik)

with open('CzasyStos.txt', 'a') as plik:
    for i in range(10, 17):
        print('Czas obslugi Kolejki dla ' + str(2**i) + ' elementow: ' + '%.4f' % CzasyStos[i-10], file=plik)

with open('CzasyLista.txt', 'a') as plik:
    for i in range(10, 17):
        print('Czas obslugi Kolejki dla ' + str(2**i) + ' elementow: ' + '%.4f' % CzasyLista[i-10], file=plik)

CzasyKolejkaLog = []
CzasyStosLog = []
CzasyListaLog = []


for i in range(0, 7):
    CzasyKolejkaLog.append(numpy.log2(CzasyKolejka[i]))
    CzasyStosLog.append(numpy.log2(CzasyStos[i]))
    CzasyListaLog.append(numpy.log2(CzasyLista[i]))
Elementy =['2^10', '2^11', '2^12', '2^13', '2^14', '2^15', '2^16']
plt.xlabel('Ilosc elementow')
plt.ylabel('log2 od czas')
plt.plot(Elementy, CzasyKolejkaLog, label='Kolejka')
plt.plot(Elementy, CzasyStosLog, label='Stos')
plt.plot(Elementy, CzasyListaLog, label='Lista')
plt.legend(loc='upper left')
plt.savefig('Wykres.pdf')
