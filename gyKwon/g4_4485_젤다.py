import heapq
def dijkstra(i,j):
    # 힙 큐 사용
    pq = []
    heapq.heappush(pq,(graph[i][j], i,j))
    # 2차원 배열 탐색하면서 다익스트라 알고리즘을 활용하여 최단 경로 찾기 활용
    while pq:
        dist, i,j = heapq.heappop(pq)
        # 다음 노드로 가능 경우의 수 들 중 최적 경로를 찾으면 다른 경로는 탐색x
        if distance[i][j] < dist:
            continue
        # 델타 탐색을 활용하여 탐색
        for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni,nj = i+di , j+dj
            if 0<=ni<n and 0<=nj<n:
                cost = graph[ni][nj]
                new_cost = cost + dist
                # 최단 거리 기록
                if distance[ni][nj] <= new_cost:
                    continue
                distance[ni][nj] = new_cost
                heapq.heappush(pq, (new_cost, ni,nj))
cnt = 1
while True:
    n= int(input())
    if not n:
        break
    graph = [list(map(int,input().split())) for _ in range(n)]


    # 누적 거리를 계속 저장
    INF = int(1e9) # 최대값으로
    distance = [[INF] * n for _ in range(n)]
    dijkstra(0,0)
    print(f'Problem {cnt}: {distance[n-1][n-1]}')
    cnt+=1