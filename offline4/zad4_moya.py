# Krzysztof Mach

from zad4testy import runtests

# tworzę nową tablicę indeksów, którą sortuję według punktu startowego elemetu tablicy T odpowiadającemu danemu indeksowi
# sortowanie: nlogn
# do elementów T będę odwoływał się przez tę tablicę (np. new_arr=[1, 0]: T[new_arr[0]] == T[1]
# nie zmienia to tablicy wejściowej a jest lepsze pamięciowo niż kopiowanie jej i sortowanie
# następnie dla każdego elementu wywołuję funkcję rec(), która to funkcja liczy tablicę o najwyższej możliwej sumie,
# jaka może powstać, jeżeli dany element weźmiemy do sumy, sprawdzam które wywołanie daje najwyższą sumę i tablicę z
# tego wywołania zwracam
#
# Powyższe rozwiązanie (bez dynamicznego): O(nlogn + 2^n)
#
# Przy pomocy tablicy f zapamiętuje wynik funkcji rec() dla danego elementu z danym pozostałym budżetem,
# w związku z czym nigdy nie obliczam funkcji rec() więcej niż raz dla danych argumentów - funkcja rec nie obliczy się
# więcej niż n*p razy
#
# Ostateczne rozwiązanie: (nlogn + np)


def select_buildings(T,p):
    n = len(T)

    # tablica indeksów
    new_arr = [i for i in range(n)]
    new_arr.sort(key=lambda x: T[x][1])

    # tablica do spamiętywania wyników
    f = [[None for w in range(p + 1)] for i in range(n)]

    def rec(index, w):
        # Sprawdzam, czy już policzone
        if f[index][w] is not None:
            return f[index][w]

        # graniczne przypadki
        if w < T[new_arr[index]][3]:
            f[index][w] = []
            return []
        if index == n - 1:
            f[index][w] = [new_arr[index]]
            return [new_arr[index]]

        # pozostałe przypadki
        max_sum = 0
        curr_arr = []
        for i in range(index + 1, n):
            if T[new_arr[index]][2] < T[new_arr[i]][1]:
                new = rec(i, w - T[new_arr[index]][3])
                new_sum = sum(T[j][0] * (T[j][2] - T[j][1]) for j in new)
                if new_sum > max_sum:
                    max_sum = new_sum
                    curr_arr = new
        max_arr = curr_arr.copy()
        max_arr.append(new_arr[index])
        f[index][w] = max_arr
        return max_arr

    max_sum = 0
    curr_arr = []
    for i in range(0, n):
        new = rec(i, p)
        new_sum = sum(T[j][0] * (T[j][2] - T[j][1]) for j in new)
        if new_sum > max_sum:
            max_sum = new_sum
            curr_arr = new

    return curr_arr


runtests( select_buildings )
