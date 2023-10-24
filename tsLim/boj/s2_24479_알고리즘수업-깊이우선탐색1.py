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
for i in range(n+1):
    gp[i].sort()
dfs(r)
for i in range(1, n+1):
    print(visited[i])


# def dfs(n, V, adj_m):
#     stack = []
#     visited = [0] * (V+1)
#     print(n)
#     visited[n] = 1
#     while True:
#         for w in range(1, V+1):
#             if adj_m[n][w] == 1 and visited[w] == 0:
#                 stack.append(n)
#                 n = w
#                 print(n)
#                 visited[n] = 1
#                 break
#         else:
#             if stack:
#                 n = stack.pop()
#             else:
#                 print('0')
#                 break
#     return
#
#
# N, M, R = map(int, sys.stdin.readline().split())
# adj_m = [[0] * (N+1) for _ in range(N+1)]
# for _ in range(M):
#     v1, v2 = map(int, sys.stdin.readline().split())
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1
# dfs(R, N, adj_m)



