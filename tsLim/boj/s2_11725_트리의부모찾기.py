# 11725
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# dfs 풀이법
def dfs(start):
    for i in adj_l[start]:
        if visited[i] == 0:
            # i 는 start의 자식노드이다.
            # 따라서 방문리스트에 부모노드의 값을 저장한다.
            visited[i] = start
            dfs(i)


N = int(input())
adj_l = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_l[a].append(b)
    adj_l[b].append(a)

# 1번부터 시작
dfs(1)

# 2번부터 출력하라 했기 때문에
for j in range(2, N+1):
    print(visited[j])