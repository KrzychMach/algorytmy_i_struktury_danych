from zad4testy import runtests


# f(b, i) = max(
#               f(b - 1, i)
#               f(b, i - 1)
#               f(b - w[i], p[i]) + s[i]
# ); b >= 0 and i >= 0
# f(b, i) = 0; b < 0 or i < 0

# gdzie b oznacza obecny budżet, i oznacza obecny akademik,
# w[i] oznacza cenę obecnego akademika
# p[i] oznacza najbliższy akademik od lewej, który nie pokrywa się z obecnym
# s[i] oznacza ilość studentów, która mieści się w obecnym akademiku


def select_buildings(T, p):
    n = len(T)
    T = [(T[i][0], T[i][1], T[i][2], T[i][3], i) for i in range(n)]
    T.sort(key=lambda x: x[2])

    f = [[[0, []] for j in range(p + 1)] for i in range(n)]

    left_neighbour = [-1] * n
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if T[j][2] < T[i][1]:
                left_neighbour[i] = j
                break

    for k in range(p + 1):
        if T[0][3] <= k:
            f[0][k][0] = T[0][0] * (T[0][2] - T[0][1])
            f[0][k][1] = [T[0][-1]]

    for i in range(1, n):
        for k in range(p + 1):
            capacity = T[i][0] * (T[i][2] - T[i][1])
            cost = T[i][3]

            f[i][k][0] = f[i - 1][k][0]
            f[i][k][1] = f[i - 1][k][1][:]

            if cost <= k:
                if f[i][k][0] < capacity:
                    f[i][k][0] = capacity
                    f[i][k][1] = [T[i][-1]]

                if left_neighbour[i] != -1 and f[i][k][0] < f[left_neighbour[i]][k - cost][0] + capacity:
                    f[i][k][0] = f[left_neighbour[i]][k - cost][0] + capacity
                    f[i][k][1] = f[left_neighbour[i]][k - cost][1][:]
                    f[i][k][1].append(T[i][-1])

    return f[n - 1][p][1]


runtests(select_buildings)
