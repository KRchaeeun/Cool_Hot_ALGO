import sys
input = sys.stdin.readline


# 매우 고전적인 옛날 방식의 dfs
def dfs(a, b, V, adj_m):
    stack = []
    visited = [0] * (V+1) # 방문목록
    visited[a] = 1 # 시작점에 1추가
    cnt = 1 # 얼마나 걸려서 갔는지 넣기 위한 cnt
    while True:
        for w in range(1, V+1):
            if adj_m[a][w] == 1:
                if visited[w] == 0:
                    stack.append(a)
                    a = w
                    visited[a] += cnt
                    cnt += 1
                    break
        else:
            # 백트래킹할때 cnt 줄여야 거리 수가 정확하게 나옴
            if stack:
                a = stack.pop()
                cnt -= 1
            else:
                break
    # 방문 안했으면 -1, 했으면 방문하는데 걸린 값 반환
    if not visited[b]:
        return -1
    else:
        return visited[b]


# N : 사람수
N = int(input())
# a, b : 촌수 계산해야 하는 두 사람
a, b = map(int, input().split())
# m : 부모자식 관계의 개수
M = int(input())
# 인접매트릭스
adj_m = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj_m[x][y] = 1
    adj_m[y][x] = 1
print(dfs(a, b, N, adj_m))