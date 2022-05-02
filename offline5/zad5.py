# Krzysztof Mach
from zad5testy import runtests

# Algorytm zachłanny, wybieram największą plamę spoścród tych, do których mogę dojechać
# Rozpatruję nie tylko plamy po ostatniej, ale wszystkie w zasięgu, czyli od 1 do fuel, gdzie fuel to zebrane dotychczas paliwo
#
# Dowód zachłannego: zakładam, że istnieje rozwiązanie, które w którymś kroku bierze plamę nie największą z dostępnych.
# Wtedy mogę zamiast niej wziąć największą, i paliwa wystarczy, żeby dojechać co najmniej do następnej plamy którą wezmę
#
# Implementuję rozwiązanie używając heapa (wiem, że można zaimportować priority queue, ale pewnie wszyscy tak zrobią,
# więc żeby uniknąć "plagiatu" zrobię kopiec. Poza tym lubie kopce). Najpierw buduję heap ze wszystkich pól, do których
# mogę dojechać ze startu i biorę największy element, czyli root. Będzie on częścią optymalnego rozwiązania.
# dołączam paliwo, które zebrałem do mojego dostępnego paliwa, dołączam do heapa nowe pola, do których mogę dojechać,
# biorę największy, dołączam paliwo itd.
# Kończę pętlę, gdy paliwo jest większe lub równe indeksowi ostatniego pola
# Zwracam posortowaną tablicę zawierającą indeksy plam, które brałem z heapa (i 0 oczywiście)
#
# funkcje heapify i add_to_heap przekleiłem do głównej, bo wywoływanie funkcji niestety kosztuje czas, tak samo rekurencja
# więc zrobiłem heapify w wersji iteracyjnej


def heapify(T, heap, root):
    """
    Nadaje odpowiednią strukturę heapowi, konkretniej subtree o początku w root.
    Tradycyjnie jest to rekurencyjne, ale zrobiłem iteracyjnie żeby było odrobinę szybciej.
    """
    while True:
        largest = root

        if root * 2 <= heap[0] and T[heap[root * 2]] > T[heap[largest]]:
            largest = root * 2

        if (root * 2) + 1 <= heap[0] and T[heap[(root * 2) + 1]] > T[heap[largest]]:
            largest = (root * 2) + 1

        if largest != root:
            heap[largest], heap[root] = heap[root], heap[largest]
            root = largest
        else:
            break


def add_to_heap(T, heap, new):
    """
    Dodaje nowy element do heap
    """
    heap[0] += 1
    heap[heap[0]] = new
    i = heap[0]
    while i // 2 > 0 and T[heap[i]] > T[heap[i // 2]]:
        heap[i], heap[i // 2] = heap[i // 2], heap[i]
        i = i // 2


def plan(T):
    stops = []
    fuel = T[0]
    stops.append(0)
    if fuel >= len(T) - 1:
        return stops

    # tworzenie początkowego max heap
    heap = [T[0]] + [j for j in range(1, len(T) + 1)]
    for j in range(heap[0] // 2, 0, - 1):
        root = j
        # przeklejona funkcja heapify, żeby działało odrobinę szybciej,
        # opisana w implementacji funkcji powyżej
        while True:
            largest = root

            if root * 2 <= heap[0] and T[heap[root * 2]] > T[heap[largest]]:
                largest = root * 2

            if (root * 2) + 1 <= heap[0] and T[heap[(root * 2) + 1]] > T[heap[largest]]:
                largest = (root * 2) + 1

            if largest != root:
                heap[largest], heap[root] = heap[root], heap[largest]
                root = largest
            else:
                break

    i = fuel + 1  # indeks następnego do dodania do heap
    stops.append(heap[1])
    fuel += T[heap[1]]
    heap[1] = heap[heap[0]]
    heap[0] -= 1
    heapify(T, heap, 1)

    while fuel < len(T) - 1:
        while i <= fuel:
            # dodanie elementu do heap
            # przeklejona funkcja add_to_heap, żeby działało odrobinę szybciej,
            # opisana w implementacji funkcji powyżej
            heap[0] += 1
            heap[heap[0]] = i
            j = heap[0]
            while j // 2 > 0 and T[heap[j]] > T[heap[j // 2]]:
                heap[j], heap[j // 2] = heap[j // 2], heap[j]
                j = j // 2

            i += 1
        stops.append(heap[1])
        fuel += T[heap[1]]
        heap[1] = heap[heap[0]]
        heap[0] -= 1
        heapify(T, heap, 1)

    return sorted(stops)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )