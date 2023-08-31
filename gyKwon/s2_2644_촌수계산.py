import sys
sys.stdin = open('input.txt')
# 너비우선탐색 함수 설정
def bfs(s,g,arr,N):
    # 방문했을시 재 방문을 피하기 위해 visited선언
    visited = [0]*(N+1)
    # visited시작값 1 대입
    visited[s] = 1
    # 시작점을 큐에 푸쉬
    q = []
    q.append(s)
    while q:
        # 큐에 들어있는 값이 목적지 값이랑 같으면 visited -1
        # 시작을 1로 했기때문에 -1 해준다
        t = q.pop(0)
        if t == g:
            return visited[t]-1
        # 1부터 N까지 탐색
        for w in range(1,N+1):
            # 서로 이어져있고 방문하지 않았을시 w를 큐에 푸쉬
            if arr[t][w] ==1 and visited[w] == 0:
                q.append(w)
                # 경로를 알기위해 이전값 더해줌
                # 좌표값에는 '1' 만 들어있기때문에 방문시 1씩 증가한다고 생각하면 된다
                visited[w] = visited[t]+1
    # 도달할 수 없는 경우 -1 리턴
    return -1

N = int(input())
s,g = map(int,input().split())
# 경로를 2차원 배열에 1로 표시
arr = [[0]*(N+1) for _ in range(N+1)]
m = int(input())
for _ in range(m):
    i,j = map(int,input().split())
    arr[i][j] = 1
    arr[j][i] = 1
# 함수 호출
print(bfs(s,g,arr,N))
