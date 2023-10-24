import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def bfs(arr):
    global people, link
    start =  arr[0]
    q = deque([start])
    # 중복방지
    visited = set([start])
    num = 0
    while q:
        v = q.popleft()
        num += people[v]
        for i in link[v]:
            if i not in visited and i in arr:
                q.append(i)
                visited.add(i)
    return num, len(visited)


N = int(input())
people = [0] + list(map(int, input().split()))
link = [[] for _ in range(N+1)]
result = float('inf')

for i in range(1, N+1):
    link[i] = list(map(int, input().split()))
    # 첫글자 버리기
    link[i] = link[i][1:]

for i in range(1, N // 2 + 1):
    # combination 사용
    combis = list(combinations(range(1, N+1), i))
    for combi in combis:
        sum1, node1 = bfs(combi)
        sum2, node2 = bfs([i for i in range(1, N+1) if i not in combi])
        if node1 + node2 == N:
            result = min(result, abs(sum1-sum2))

if result != float('inf'):
    print(result)
else:
    print(-1)