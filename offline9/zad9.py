from zad9testy import runtests
from collections import deque


def ff15(G, s):
    residual_g = [[G[i][j] for j in range(len(G))] for i in range(len(G))]
    total = 0
    q = deque()

    while True:
        visited = [False] * len(G)
        path = [None] * len(G)
        q.append(s)
        visited[s] = True

        found_path = False
        while q:
            v = q.popleft()
            if residual_g[v][-1]:
                path[-1] = v
                found_path = True
                q.clear()
                break
            for u in range(len(G) - 1):
                if not visited[u] and residual_g[v][u]:
                    visited[u] = True
                    path[u] = v
                    q.append(u)
        if found_path is False:
            return total

        curr_flow = float('inf')
        v = path[-1]
        while path[v] is not None:
            curr_flow = min(curr_flow, residual_g[path[v]][v])
            v = path[v]

        v = path[-1]
        while path[v] is not None:
            residual_g[path[v]][v] -= curr_flow
            v = path[v]

        total += curr_flow


def maxflow(G, s):
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
            flow = ff15(mac_g, s)
            if flow > max_flow:
                max_flow = flow
            mac_g[u][-1] = 0
        mac_g[v][-1] = 0
    return max_flow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
