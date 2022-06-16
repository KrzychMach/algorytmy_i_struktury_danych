# Krzysztof Mach
from zad9testy import runtests
from collections import deque


"""
Brute force, dla każdych 2 wierzchołków sprawdzam max flow, zwracam największy
złożoność: O(V^3 * E^2)
"""


def maxflow(G, s):
    q = deque()
    n = max(max(i[0], i[1]) for i in G) + 1
    mac_g = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for v, u, f in G:
        mac_g[v][u] = f

    max_flow = 0
    for v in range(n):
        if v == s:
            continue
        mac_g[v][-1] = 1
        for u in range(v + 1, n):
            if u == s:
                continue
            mac_g[u][-1] = 1

            residual_g = [mac_g[i][:] for i in range(n + 1)]
            total = 0

            while True:
                visited = [False] * len(mac_g)
                path = [-1] * len(mac_g)
                q.append(s)
                visited[s] = True

                while q:
                    x = q.popleft()
                    if residual_g[x][-1]:
                        path[-1] = x
                        q.clear()
                        break
                    for y in range(len(mac_g) - 1):
                        if not visited[y] and residual_g[x][y]:
                            visited[y] = True
                            path[y] = x
                            q.append(y)
                else:
                    break

                curr_flow = float('inf')
                x = path[-1]
                while path[x] != -1:
                    curr_flow = min(curr_flow, residual_g[path[x]][x])
                    x = path[x]

                x = path[-1]
                while path[x] != -1:
                    residual_g[path[x]][x] -= curr_flow
                    x = path[x]

                total += curr_flow

            if total > max_flow:
                max_flow = total

            mac_g[u][-1] = 0
        mac_g[v][-1] = 0
    return max_flow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
