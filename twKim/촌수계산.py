import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
n += 1
start, end = map(int, input().split())
matrix = [[0]*n for _ in range(n)]
visited = [-1]*n
k = int(input())

for i in range(k):
    a,b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

q = deque([])
q.append(start)
visited[start] = 0

while q :

    s = q.popleft()

    if s == end:
        break

    for e in range(n):
        if matrix[s][e] and visited[e] == -1:
            visited[e] = visited[s] + 1
            q.append(e)

print(visited[end])