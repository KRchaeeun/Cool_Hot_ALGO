from collections import deque


def solution(n, m, x, y, r, c, k):
    answer = ''

    def manhattan(i, j):
        return abs(i - (r - 1)) + abs(j - (c - 1))

    if manhattan(x - 1, y - 1) > k or (manhattan(x - 1, y - 1) - k) % 2:
        return 'impossible'
    dir = {(1, 0): 'd', (0, -1): 'l', (0, 1): 'r', (-1, 0): 'u'}
    q = deque()
    q.append((x - 1, y - 1, 0, ''))
    while q:
        si, sj, cnt, moon = q.popleft()
        if (si, sj) == (r - 1, c - 1) and (k - cnt) % 2:
            return 'impossible'
        elif (si, sj) == (r - 1, c - 1) and cnt == k:
            return moon
        for di, dj in dir:
            ni, nj = si + di, sj + dj
            if 0 <= ni < n and 0 <= nj < m:
                if manhattan(ni, nj) + cnt + 1 > k:
                    continue
                q.append((ni, nj, cnt + 1, moon + dir[(di, dj)]))
                break

    return answer