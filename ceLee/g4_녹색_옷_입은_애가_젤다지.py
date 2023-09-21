import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 델타: 상하좌우
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 다익스트라
def Daijkstra(x, y, N):
    heap = []
    dist[x][y] = my_map[x][y]  # 시작점 dist 갱신
    heappush(heap, (0, x, y))  # push
    while heap:  # heap에 원소가 있는 동안 while문 반복
        w, i, j = heappop(heap)  # pop
        if dist[i][j] < w:  # 불필요한 계산 안하기 위해 이미 저장되어있는 값이 더 작으면 패스
            continue
        for di, dj in delta: # 델타 검색
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:  # 배열안에 있으면
                next_dist = dist[i][j] + my_map[ni][nj]  # 가중치 더하고
                if dist[ni][nj] <= next_dist:  # 가중치 더한값보다 저장되어있는 값이 작으면 패스
                    continue
                dist[ni][nj] = next_dist  # 가중치 더한값보다 저장되어있는 값이 크면 dist 갱신
                heappush(heap, (next_dist, ni, nj))  # push
tc = 1
while True:
    N = int(input())  # N: 동굴의 크기
    if N == 0:  # 종료문
        break
    my_map = [list(map(int, input().split())) for _ in range(N)]  # 정보 입력
    dist = [[float("inf")] * N for _ in range(N)]  # dist의 초기값 무한
    Daijkstra(0, 0, N)  # 다익스트라 호출
    # 출력
    print(f"Problem {tc}: {dist[N-1][N-1]}")
    tc += 1