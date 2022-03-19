# Krzysztof Mach

from zad2testy import runtests


def depth(L):
    groups = []
    sort(L, 0, len(L) - 1)
    for interval in L:
        flag = 1
        for group in groups:
            if interval[0] >= group[0][0] and interval[1] <= group[0][1]:
                flag = 0
                group[1] += 1
        if flag:
            groups.append([interval, 0])
    return max([i[1] for i in groups])


# ten konkretny sort będzie sortował według key = lambda x: x[1] - x[0], reverse = True
# bo tak najlepiej w przypadku mojego algorytmu
# jest to połączenie quick sort i insertion sort, dla fragmentu tablicy do posortowania < 18 przechodzi na insertion
# liczba 18 wybrana arbitralnie, według testów dla 18 właśnie jest najszybciej
def sort(arr: list, start: int, end: int):
    while start < end:
        if end - start < 18:
            for i in range(start + 1, end + 1):
                while i > start and arr[i][1] - arr[i][0] > arr[i - 1][1] - arr[i - 1][0]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    i -= 1
            return
        else:
            pivot = start + (end - start) // 2
            arr[pivot], arr[end] = arr[end], arr[pivot]
            j = start
            for i in range(start, end):
                if arr[i][1] - arr[i][0] > arr[end][1] - arr[end][0]:
                    arr[i], arr[j] = arr[j], arr[i]
                    j += 1
            arr[j], arr[end] = arr[end], arr[j]
            sort(arr, start, j - 1)
            start = j + 1


runtests( depth )
