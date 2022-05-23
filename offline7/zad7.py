# Krzysztof Mach
from zad7testy import runtests


# szukam de facto cyklu Hamiltona z dodatkowymi warunkami
# Sprawdzam wszystkie możliwe ścieżki, czyli permutacje wierzchołków,
# i zwracam pierwszą znalezioną

# złożoność: O(V!)

# z racji, że poprawna ścieżka ma zawsze długość V, nie muszę rekonstruować jej przy pomocy parentów,
# po prostu mam jedną tablicę path, której pola nadpisuję zależnie od ścieżki, którą obecne sprawdzam


def droga(G):
    n = len(G)

    visited = [False for i in range(n)]
    visited[0] = True
    path = [0 for i in range(n)]

    def hamilton(i, v, direction, initial_dir):
        """
        Zwraca True, jeżeli udało się znaleźć poprawną ścieżkę, w przeciwnym wypadku False
        """
        nonlocal visited, path
        path[i] = v

        if i == n - 1:
            if 0 in G[v][direction] and v in G[0][1 - initial_dir]:
                return True
            else:
                return False

        for neighbor in G[v][direction]:
            if not visited[neighbor]:
                next_direction = 1 if v in G[neighbor][0] else 0
                visited[neighbor] = True
                if hamilton(i + 1, neighbor, next_direction, initial_dir):
                    return True
                visited[neighbor] = False

        return False

    for i in (0, 1):
        ans = hamilton(0, 0, i, i)
        if ans:
            return path

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)
