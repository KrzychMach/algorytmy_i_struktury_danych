# Krzysztof Mach
#
# Z pierwszych k+1 elementów listy tworzę min-heap (nie wiem jak po polsku niestety)
# Najmniejszy element z heap (czyli dla min-heap będzie to korzeń) dołączam do posortowanej listy
# Dołączam do heap kolejny element, znowu robię min-heap itd.
#
# Druga wersja programu. W pierwszej rozbiłem funkcję główną na parę funkcji składowych.
# Było to dużo bardziej czytelne, ale niestety wolniejsze,
# bo wywoływanie funkcji w Pythonie jest dużo "droższe" niż w innych językach.
# (różnica ok. 0,2s na ostatnim teście)
# Jeśli osoba sprawdzająca chce, to mogę wysłać też wersję 1.0 - wolniejsza, ale moim zdaniem dużo czytelniejsza
# Ja zazwyczaj kładę priorytet na czytelność, ale niestety bezlitosne testy skłoniły mnie do złych, ale szybkich praktyk
from zad1testy import Node, runtests


def SortH(p, k):
    if p is None or k == 0:
        return p
    elif p.next is None:
        return p

    # Tworzy listę odniesień do instancji klasy Node
    node = p
    heap = [None for _ in range(k + 1)]
    for i in range(k + 1):
        heap[i] = node
        node = node.next
        if node is None:
            break

    if heap[len(heap) - 1] is None:  # Na wypadek, gdy k == n
        del heap[len(heap) - 1]

    for i in range((len(heap) - 1) // 2, -1, -1):  # nadaje poprawną strukturę (min-heap)
        heapify(heap, i)

    for i in range(len(heap)):
        p = p.next

    new_list_head = None
    curr_node = None
    while heap:
        if new_list_head is not None:  # dołączam najmniejszy element do zwracanej listy
            curr_node.next = heap[0]
            curr_node = curr_node.next
        else:                          #
            curr_node = heap[0]
            new_list_head = curr_node
        # Wstawiam następny Node do heap
        if p is not None:
            heap[0] = p
        else:
            heap[0] = heap[len(heap) - 1]
            del heap[len(heap) - 1]
        heapify(heap, 0)  # "Naprawiam" heap
        if p is not None:
            p = p.next
    curr_node.next = None
    return new_list_head


# Przywraca poprawną strukturę, tj. najmniejszy element  w root
def heapify(heap, root):
    min_node = root
    if 2 * root + 1 < len(heap) and heap[min_node].val > heap[2 * root + 1].val:
        min_node = 2 * root + 1
    if 2 * root + 2 < len(heap) and heap[min_node].val > heap[2 * root + 2].val:
        min_node = 2 * root + 2
    if min_node != root:
        heap[root], heap[min_node] = heap[min_node], heap[root]  # najmniejszy element w roocie, stary root pod indeksem min_node
        heapify(heap, min_node)  # rekurencyjne wywołanie dla starego roota


runtests(SortH)
