import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(start):
    global cnt

    visited[start] = cnt
    cnt += 1
    for w in gp[start]:
        if not visited[w]:
            dfs(w)


n, m, r = map(int, input().split())
gp = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1
for _ in range(m):
    u, v = map(int, input().split())
    gp[u].append(v)
    gp[v].append(u)

for i in range(n+1): gp[i].sort()

dfs(r)

for i in range(1, n+1):
    print(visited[i])
