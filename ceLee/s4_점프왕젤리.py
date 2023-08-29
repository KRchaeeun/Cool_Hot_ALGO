import sys
sys.stdin = open("input.txt")

from collections import deque
# 델타 (오른쪽 아래)
di = [0, 1]
dj = [1, 0]

def BFS(i, j):

    # queue: [x좌표, y좌표] 삽입할 리스트
    queue = deque()
    queue.append([i, j])

    # BFS 시작
    while queue:  # queue이 빌때까지 while문 반복
        x, y = queue.popleft()  # stack 저장되어있는 x좌표와 y좌표를 pop하고 x, y에 저장
        num_jelly = graph[x][y]  # 현재 위치의 젤리수를 num_jelly에 저장

        # 종료문
        if graph[x][y] == -1:  # -1에 도착하면 True 반환
            return True

        for d in range(2):  # 델타 검색 총 2개
            nx = x + di[d]*num_jelly
            ny = y + dj[d]*num_jelly

            # nx, ny가 배열을 넘지 않고 방문한 적이 없을 때(visited[nx][ny] = 0)
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문 표시로 1로 바꾸어주고
                queue.append([nx, ny])  # 이 점에서 델타 탐색을 해야하므로 x좌표와 y좌표를 stack에 저장

N = int(input())  # 배열의 크기 N X N
graph = [list(map(int, input().split())) for _ in range(N)]
visited =[[0] * N for _ in range(N)]  # visited: 방문을 표시할 배열

# 출력
if BFS(0,0):  # 도착점을 찾으면
    print('HaruHaru')
else:  # 찾지 못하면
    print('Hing')