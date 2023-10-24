from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    visited = [0] * (N + 1)
    visited[s] = 1
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        for k in arr[s]:
            if visited[k] ==0:
                q.append(k)
                visited[q] = 1

N = int(input())
heads = list(map(int,input().split()))
arr = [[] for _ in range(N)]
fina1 = []
fina2 = []
for i in range(1,N+1):
    ra = list(map(int,input().split()))
    for j in len(ra):
        arr[i].append(ra[j])
        # arr[ra[j]].append(i)