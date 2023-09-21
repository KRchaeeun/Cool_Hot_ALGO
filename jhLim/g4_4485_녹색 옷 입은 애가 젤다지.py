import sys, heapq
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dij():
    heap = []
    heapq.heappush(heap, (cave[0][0], 0, 0))
    path[0][0] = cave[0][0]

    while heap:
        r, x, y = heapq.heappop(heap)

        if path[x][y] < r:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                nr = r + cave[nx][ny]
                if path[nx][ny] > nr:
                    path[nx][ny] = nr
                    heapq.heappush(heap, (nr, nx, ny))


N = int(input().rstrip())
cnt = 0

while N != 0:
    cnt += 1
    cave = [list(map(int, input().rstrip().split())) for _ in range(N)]
    path = [[float('inf')] * N for _ in range(N)]

    dij()

    print(f'Problem {cnt}: {path[N-1][N-1]}')

    N = int(input().rstrip())