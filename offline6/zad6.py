import collections
from zad6testy import runtests


def bfs(G, s, t, to_ignore=(None, None)):
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
            if (curr, next_vertex) == to_ignore or (next_vertex, curr) == to_ignore:
                continue
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

    return shortest_path[::-1]


def longer(G, s, t):
    shortest_path = bfs(G, s, t)
    if len(shortest_path) == 0:
        return None

    for i in range(1, len(shortest_path)):
        curr_tuple = (shortest_path[i - 1], shortest_path[i])
        curr_path = bfs(G, s, t, to_ignore=curr_tuple)
        if len(curr_path) == 0 or len(curr_path) > len(shortest_path):
            return curr_tuple

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
