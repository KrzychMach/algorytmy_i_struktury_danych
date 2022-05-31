from math import ceil
from zad8testy import runtests


def find(parents, v):
    while parents[v] != v:
        v = parents[v]
    return v


def union(parents, v, u):
    p_v = find(parents, v)
    p_u = find(parents, u)
    parents[p_u] = p_v


def kruskal(G, num_of_vertices):
    mst_len = 0
    parents = [i for i in range(len(G))]
    min_val = float('inf')
    max_val = -1
    for d, s, t in G:
        p_s = s
        while parents[p_s] != p_s:
            p_s = parents[p_s]
        p_t = t
        while parents[p_t] != p_t:
            p_t = parents[p_t]
        if p_s != p_t:
            mst_len += 1
            min_val = min(min_val, d)
            max_val = max(max_val, d)
            parents[p_t] = p_s
            if mst_len == num_of_vertices - 1:
                return max_val - min_val
    return max_val - min_val


def highway(A):
    n = len(A)
    G = []

    for i in range(n):
        for j in range(i + 1, n):
            dist = ceil(((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** 0.5)
            G.append((dist, i, j))

    new_G = G.copy()
    min_diff = float('inf')
    for e in G:
        new_G.sort(key=lambda x: abs(e[0] - x[0]))
        min_diff = min(min_diff, kruskal(new_G, n))

    return min_diff


runtests(highway, all_tests=True)
