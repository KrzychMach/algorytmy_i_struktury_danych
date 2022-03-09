# Krzysztof Mach
#
# Z pierwszych k+1 elementów listy tworzę min-heap (nie wiem jak po polsku niestety)
# Najmniejszy element z heap (czyli dla min-heap będzie to korzeń) dołączam do posortowanej listy
# Dołączam do heap kolejny element, znowu robię min-heap itd.
from zad1testy import Node, runtests


def SortH(p, k):
    if p is None or k == 0:
        return p
    elif p.next is None:
        return p
    return heap_sort(p, k)


# Tworzy listę instancji klasy Node (konkretniej odniesień do instancji) o długości size zaczynając od node
# następnie nadaje mu odpowiednią strukturę, tj. najmniejszy element u góry
def create_heap(node, size):
    heap = [None for i in range(size)]
    for i in range(size):
        heap[i] = node
        node = node.next
        if node is None:
            break
    while heap[len(heap) - 1] is None:
        del heap[len(heap) - 1]
    for i in range((len(heap) - 1) // 2, -1, -1):  # nadaje poprawną strukturę
        heapify(heap, i)
    return heap


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


def replace_root_node(heap, new):
    if new is not None:
        heap[0] = new
    else:
        heap[0] = heap[len(heap) - 1]
        del heap[len(heap) - 1]
    heapify(heap, 0)  # "Naprawiam" cały heap


def heap_sort(p, k):
    min_heap = create_heap(p, k + 1)
    for i in range(len(min_heap)):
        p = p.next
    new_list_head = None
    curr_node = None
    while min_heap:
        if new_list_head is not None:
            curr_node.next = min_heap[0]
            curr_node = curr_node.next
        else:
            curr_node = min_heap[0]
            new_list_head = curr_node
        replace_root_node(min_heap, p)
        if p is not None:
            p = p.next
    curr_node.next = None
    return new_list_head


runtests(SortH)
