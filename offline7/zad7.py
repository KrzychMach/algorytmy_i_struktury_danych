from zad7testy import runtests


def droga(G):
    n = len(G)

    visited = [False for i in range(n)]
    visited[0] = True
    path = [0 for i in range(n)]

    def hamilton(i, v, direction, initial_dir):
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
                # continuation = hamilton(i + 1, neighbor, next_direction, initial_dir)
                # if continuation:
                #     return continuation
                if hamilton(i + 1, neighbor, next_direction, initial_dir):
                    return True
                visited[neighbor] = False

        return False

    for i in (0, 1):
        # for neighbor in G[0][i]:
        #     next_direction = 1 if 0 in G[neighbor][0] else 0
        #     visited[neighbor] = True
        #     temp = hamilton(1, neighbor, next_direction, i)
        #     if temp:
        #         return temp
        #     visited[neighbor] = False
        ans = hamilton(0, 0, i, i)
        if ans:
            return path

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)
