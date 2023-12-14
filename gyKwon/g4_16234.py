from collections import deque
import sys

input = sys.stdin.readline
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def bfs():
    global cnt
    while True:
        flag = False
        q = deque()
        visited = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    q.append((i, j))
                    alliance = [(i, j)]
                    nums = 1
                    suma = arr[i][j]
                    while q:
                        ai, aj = q.popleft()
                        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                            ni, nj = ai + di, aj + dj
                            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and l <= abs(arr[ai][aj] - arr[ni][nj]) <= r:
                                visited[ni][nj] = 1
                                alliance.append((ni, nj))
                                nums += 1
                                suma += arr[ni][nj]
                                q.append((ni, nj))
                    if nums > 1:
                        flag = True
                        for fi, fj in alliance:
                            arr[fi][fj] = suma // nums
        if not flag:
            break
        cnt += 1
    return

bfs()

print(cnt)
