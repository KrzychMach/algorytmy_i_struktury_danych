# Krzysztof Mach
import collections
from zad6testy import runtests


# Szuka najkrótszej ścieżki z s do t, następnie po kolei ignoruje jedną krawędź ze znalezionej ścieżki i sprawdza,
# czy najkrótsza ścieżka się wydłużyła. Jeżeli tak, to zwraca tę krawędź.
#
# Złożoność BFS: O(V+E)
# wywołuję BFS raz, by znaleźć ścieżkę, a następnie wywołuję BFS dla każdej krawędzi w ścieżce. Ścieżka w najgorszym
# wypadku ma długość E, więc złożoność:
# O(E * (V + E))
#
# Tak jak w innych zadaniach przekleliłem kod funkcji bfs do funkcji głównej, bo przyspiesza to kod.
# Mimo że nie pełni ona żadnej roli, zostawiam funckje bfs dla czytelności

# def bfs(G, s, t, to_ignore=(None, None)):
#     """
#     BFS do szukania najkrótszej ścieżki z s do t w grafie G
#     ignoruje krawędź przekazaną jako argument to_ignore, domyślnie nie ignoruje nic
#     """
#     n = len(G)
#     start = s
#     end = t
#     q = collections.deque()
#     q.append(start)
#
#     distance = [-1 for _ in range(n)]
#     visited = [False for _ in range(n)]
#     prev = [None for _ in range(n)]
#     visited[start] = True
#     distance[start] = 0
#
#     while q:
#         curr = q.popleft()
#
#         if curr == end:
#             break
#
#         for next_vertex in G[curr]:
#             if (curr, next_vertex) == to_ignore or (next_vertex, curr) == to_ignore:
#                 continue
#             if not visited[next_vertex]:
#                 distance[next_vertex] = distance[curr] + 1
#                 prev[next_vertex] = curr
#                 visited[next_vertex] = True
#                 q.append(next_vertex)
#
#     shortest_path = []
#     if prev[t] is None:
#         return []
#     i = end
#     while True:
#         shortest_path.append(i)
#         if prev[i] is not None:
#             i = prev[i]
#         else:
#             break
#
#     return shortest_path[::-1]


def longer(G, s, t):
    n = len(G)
    start = s
    end = t
    q = collections.deque()
    q.append(start)

    distance = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    prev = [None for _ in range(n)]
    visited[start] = True
    distance[start] = 0

    while q:
        curr = q.popleft()

        if curr == end:
            break

        for next_vertex in G[curr]:
            if not visited[next_vertex]:
                distance[next_vertex] = distance[curr] + 1
                prev[next_vertex] = curr
                visited[next_vertex] = True
                q.append(next_vertex)

    shortest_path = []
    if prev[t] is None:
        return []
    i = end
    while True:
        shortest_path.append(i)
        if prev[i] is not None:
            i = prev[i]
        else:
            break

    # shortest_path = shortest_path[::-1]

    if len(shortest_path) == 0:
        return None

    for i in range(1, len(shortest_path)):
        curr_tuple = (shortest_path[i - 1], shortest_path[i])
        q = collections.deque()
        q.append(start)

        distance = [-1 for _ in range(n)]
        visited = [False for _ in range(n)]
        prev = [None for _ in range(n)]
        visited[start] = True
        distance[start] = 0

        while q:
            curr = q.popleft()

            if curr == end:
                break

            for next_vertex in G[curr]:
                if (curr, next_vertex) == curr_tuple or (next_vertex, curr) == curr_tuple:
                    continue
                if not visited[next_vertex]:
                    distance[next_vertex] = distance[curr] + 1
                    prev[next_vertex] = curr
                    visited[next_vertex] = True
                    q.append(next_vertex)

        curr_path = []
        if prev[t] is None:
            return curr_tuple
        i = end
        while True:
            curr_path.append(i)
            if prev[i] is not None:
                i = prev[i]
            else:
                break

        if len(curr_path) > len(shortest_path):
            return curr_tuple

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
