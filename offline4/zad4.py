# Krzysztof Mach
from zad4testy import runtests


def select_buildings_proto(T, p):
    n = len(T)
    f = [[[0, []] for j in range(p + 1)] for i in range(n)]
    T = [(h, a, b, w, h * (b - a)) for h, a, b, w in T]
    for w in range(p + 1):
        if w >= T[0][3]:
            f[0][w][0] += T[0][0] * (T[0][2] - T[0][1])
            f[0][w][1].append(0)

    for i in range(1, n):
        for w in range(1, p + 1):
            if w < T[i][3]:
                f[i][w][0] = f[i - 1][w][0]
                f[i][w][1] = (f[i - 1][w][1]).copy()
            else:

                flag = 1
                for building in f[i - 1][w - T[i][3]][1]:
                    if T[building][1] <= T[i][1] <= T[building][2] or T[building][1] <= T[i][2] <= T[building][2] or \
                            T[i][1] <= T[building][1] <= T[i][2] or T[i][1] <= T[building][2] <= T[i][2]:
                        flag = 0
                        break

                if flag:
                    if f[i - 1][w - T[i][3]][0] + (T[i][0] * (T[i][2] - T[i][1])) > f[i - 1][w][0] or \
                        (f[i - 1][w - T[i][3]][0] + (T[i][0] * (T[i][2] - T[i][1])) == f[i - 1][w][0] and
                            sum(T[j][3] for j in f[i - 1][w - T[i][3]][1]) < sum(T[j][3] for j in f[i - 1][w][1])):
                        f[i][w][0] = f[i - 1][w - T[i][3]][0] + (T[i][0] * (T[i][2] - T[i][1]))
                        f[i][w][1] = (f[i - 1][w - T[i][3]][1]).copy()
                        f[i][w][1].append(i)
                    else:
                        f[i][w][0] = f[i - 1][w][0]
                        f[i][w][1] = (f[i - 1][w][1]).copy()
                else:
                    if f[i - 1][w][0] < T[i][0] * (T[i][2] - T[i][1]) or \
                            (f[i - 1][w][0] == T[i][0] * (T[i][2] - T[i][1]) and
                                sum(T[j][3] for j in f[i - 1][w][1]) >= T[i][3]):
                        f[i][w][0] = T[i][0] * (T[i][2] - T[i][1])
                        f[i][w][1] = [i]
                    else:
                        f[i][w][0] = f[i - 1][w][0]
                        f[i][w][1] = (f[i - 1][w][1]).copy()

    return (f[n - 1][p][1]).copy()


def select_buildings(T, p):
    n = len(T)
    new_arr = [(T[i][0] * (T[i][2] - T[i][1]), T[i][1], T[i][2], T[i][3], i) for i in range(n)]
    new_arr.sort(key=lambda x: x[0])

    f = [[[0, []] for j in range(p + 1)] for i in range(n)]
    for w in range(p + 1):
        if w >= T[0][3]:
            f[0][w][0] += new_arr[0][0]
            f[0][w][1].append(new_arr[0][4])

    return



runtests(select_buildings)
