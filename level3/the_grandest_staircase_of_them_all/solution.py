def solution(n):
    smap = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    smap[0][0] = 1
    for y in range(1, n + 1):
        for x in range(n + 1):
            smap[y][x] = smap[y - 1][x]
            if x >= y:
                smap[y][x] += smap[y - 1][x - y]
    return smap[n][n] - 1
