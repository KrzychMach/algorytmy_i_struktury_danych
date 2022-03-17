# Krzysztof Mach

from zad2testy import runtests


def depth(L):



# będę sortował tablicę dwuwymiarową, key jest indeksem wartości w drugim wymiarze względem której sortuje
def quicksort(array: list, start: int, end: int, key: int):
    while start < end:
        pivot = (end - start + 1) // 2 + start  # środkowy element jako pivot
        array[pivot], array[end] = array[end], array[pivot]
        pivot_start = end  # w celu poprawienia czasu nie będę sortował elementów równych pivotowi
        pivot_end = end  # w celu poprawienia czasu nie będę sortował elementów równych pivotowi
        j = start  # miejsce, w które wstawić następny element mniejszy od pivot
        for i in range(start, end):
            if array[i][key] < array[end][key]:
                array[i], array[j] = array[j], array[i]
                j += 1
            elif array[i][key] == array[end][key]:
                array[i], array[pivot_start - 1] = array[pivot_start - 1], array[i]
        array[j], array[end] = array[end], array[j]  # teraz element pivot pod indeksem j
        pivot = j  # indeks pivot teraz jest tam, gdzie element pivot
        quicksort(array, start, pivot - 1, key)
        start = pivot + 1


runtests( depth )
