from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, group):
    q = deque()
    q.append(start)
    visited[start] = group
    while q:
        x = q.popleft()
        for i in graph[x]:
            # 여기가 뒤집기 과정, 이를 통해서 같은 집합이 안되도록 만듬
            if not visited[i]:
                q.append(i)
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]:
                return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (V+1)

    for i in range(1, V+1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break

    if result:
        print('YES')
    else:
        print('NO')
