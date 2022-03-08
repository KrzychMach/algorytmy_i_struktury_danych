# Krzysztof Mach
#
# Z pierwszych k+1 elementów listy tworzę min-heap (nie wiem jak po polsku niestety)
# Najmniejszy element z heap (czyli dla min-heap będzie to korzeń) dołączam do posortowanej listy
# Dołączam do heap kolejny element, znowu robię min-heap itd.
#
# Klasa oczywiście niepotrzebna, bo będzie tylko jeden heap, więc lepiej by było funkcjami, ale to tak na przyszłość
# Poza tym lubię OOP w pythonie :)
from zad1testy import Node, runtests


class MinHeap(list):
    def __init__(self, array):
        super().__init__(array)
        self.remaining = len(array)  # Niepotrzebne, mógłbym usuwać ostatnie elementy, ale nie wiem czy mogę używać del i append
        self._minify()

    def _minify(self):
        changes = 1
        while changes:  # wykonuje się, dopóki w poprzedniej iteracji zostały zamienione jakieś elementy
            changes = 0
            for i in range((self.remaining - 2) // 2, -1, -1):
                try:
                    if self[i].val > self[2 * i + 1].val:
                        changes = 1
                        self[i], self[2 * i + 1] = self[2 * i + 1], self[i]  # Zamiana dziecka i rodzica
                        continue
                    if self[i].val > self[2 * i + 2].val:
                        changes = 1
                        self[i], self[2 * i + 2] = self[2 * i + 2], self[i]  # Zamiana dziecka i rodzica
                        continue
                except IndexError:
                    pass
                except AttributeError:
                    pass

    def replace_last_node(self, new):
        self[self.remaining - 1] = new
        if new is None:
            self.remaining -= 1
        self._minify()

    def get_min(self):
        min_node = self[0]
        self[0] = self[self.remaining - 1]
        return min_node


def SortH(p, k):
    if p is None or k == 0:
        return p
    elif p.next is None:
        return p
    temp_node = p
    list_length = 0
    while temp_node is not None:
        list_length += 1
        temp_node = temp_node.next
    min_heap = create_heap(p, min(k + 1, list_length))
    for i in range(min_heap.remaining):
        p = p.next
    new_list_head = None
    curr_node = None
    while min_heap.remaining > 0:
        if new_list_head is None:
            curr_node = min_heap.get_min()
            new_list_head = curr_node
        else:
            curr_node.next = min_heap.get_min()
            curr_node = curr_node.next
        min_heap.replace_last_node(p)
        if p is not None:
            p = p.next
    curr_node.next = None
    return new_list_head


# Tworzy listę instancji klasy Node o długości size zaczynając od node, przekazuje ją do konstruktora MinHeap
def create_heap(node, size):
    heap_template = [None for i in range(size)]
    for i in range(size):
        heap_template[i] = node
        node = node.next
    return MinHeap(heap_template)


runtests( SortH )
