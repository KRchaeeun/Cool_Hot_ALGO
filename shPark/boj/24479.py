import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(start):
    # 방문순서를 글로벌 변수로 선언
    global cnt
    # 방문표시를 True 나 1 대신 방문순서로 대체
    visited[start] = cnt
    cnt += 1
    # 차례대로 방문
    for w in gp[start]:
        # 방문하지 않았을 경우만
        if not visited[w]:
            dfs(w)


# 입력
n, m, r = map(int, input().split())
# 그래프 초기화
gp = [[] for _ in range(n+1)]
# 방문체크용
visited = [0] * (n+1)
# 방문순서
cnt = 1
# 그래프 노드 연결
for _ in range(m):
    u, v = map(int, input().split())
    gp[u].append(v)
    gp[v].append(u)
# 오름차순으로 정렬
for i in range(n+1):
    gp[i].sort()
# 탐색
dfs(r)
# 출력
for i in range(1, n+1):
    print(visited[i])
