# Krzysztof Mach
from zad8testy import runtests
from math import ceil


"""
Szukam maksymalnego drzewa rozpinającego, później dla każdego brzegu (s, t) niebędącego w drzewie szukam DFSem 
najdłużego brzegu w ścieżce z s do t w drzewie, usuwam je, dodaję brzeg (s, t).
Po każdej zmianie obliczam różnicę między najdłuższym i najkrótszym brzegiem, na koniec zwracam najmniejszą znalezioną.
Złożoność: O(n^3), gdzie n - liczba miast. Niestety stała gigantyczna.
"""


def highway(A):
    def dfs(G, s, t):
        if s == t:
            return 0, s, t

        for neighbor, w in list_G[s]:
            if not visited[neighbor]:
                visited[neighbor] = True
                result = dfs(G, neighbor, t)
                if result:
                    return (w, s, neighbor) if w > result[0] else result
        return False

    n = len(A)
    if n == 1 or n == 2:
        return 0
    G = []

    for i in range(n):
        for j in range(i + 1, n):
            edge_len = ceil(((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** 0.5)
            G.append((i, j, edge_len))

    G.sort(key=lambda x: x[2], reverse=True)
    parents = list(range(len(G)))
    mst = []

    for s, t, w in G:
        parent_s = s
        while parents[parent_s] != parent_s:
            parent_s = parents[parent_s]
        parent_t = t
        while parents[parent_t] != parent_t:
            parent_t = parents[parent_t]
        if parent_s != parent_t:
            mst.append((s, t, w))
            parents[parent_t] = parent_s
            if len(mst) == n - 1:
                break

    list_G = [[] for i in range(n)]
    for s, t, w in mst:
        list_G[s].append((t, w))
        list_G[t].append((s, w))
    min_diff = (max(i[2] for i in mst) - min(i[2] for i in mst))

    for i in range(len(G)):
        if G[i] in mst:
            continue

        visited = [False] * n
        visited[G[i][0]] = True
        _, x, y = dfs(list_G, G[i][0], G[i][1])

        for j in range(len(list_G[x])):
            if list_G[x][j][0] == y:
                del list_G[x][j]
                break
        for j in range(len(list_G[y])):
            if list_G[y][j][0] == x:
                del list_G[y][j]
                break

        list_G[G[i][0]].append((G[i][1], G[i][2]))
        list_G[G[i][1]].append((G[i][0], G[i][2]))

        high = 0
        low = float('inf')
        for j in range(n):
            for _, w in list_G[j]:
                high = max(high, w)
                low = min(low, w)

        min_diff = min(min_diff, high - low)

    return min_diff


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(highway, all_tests=True)
