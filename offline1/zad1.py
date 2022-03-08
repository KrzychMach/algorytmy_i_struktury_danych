# Krzysztof Mach
#
# Z pierwszych k+1 elementów listy tworzę min heap (nie wiem jak po polsku niestety)
# Najmniejszy element z heap (czyli dla min heap będzie to korzeń) dołączam do posortowanej listy
# Dołączam do heap kolejny element, znowu robię min heap itd.
#
# Heap będę przechowywał w tablicy (pythonowa lista, ale u mnie będzie stałej długości)
# dla elementu pod indeksem i:
#   rodzic: (i - 1) // 2
#   dzieci: 2 * i, 2 * i + 1
from zad1testy import Node, runtests


def SortH(p, k):

    pass


runtests( SortH ) 
