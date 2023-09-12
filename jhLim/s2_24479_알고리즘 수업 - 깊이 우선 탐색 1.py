import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(start):
    global cnt
    visited[start] = cnt
    cnt += 1
    for w in arr[start]:
        if not visited[w]:
            dfs(w)


N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

# 입력받은 노드를 연결
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

# 오름차순으로 정렬하기 위해 리스트 내부값을 정렬
for i in range(N+1):
    arr[i].sort()

dfs(R)

for j in range(1, N+1):
    print(visited[j])