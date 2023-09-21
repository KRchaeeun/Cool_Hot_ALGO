import sys
input = sys.stdin.readline

import heapq

V, E = map(int, input().split())
nodes = [[] for _ in range(V)]
visited = [0] * V

for i in range(E):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].append((c, b))
    nodes[b].append((c, a))

heap = []
heapq.heappush(heap, (0, 0))
sum_w = 0

while heap:

    w, s = heapq.heappop(heap)

    if visited[s]:
        continue

    visited[s] = 1

    sum_w += w

    for i in nodes[s]:
        if visited[i[1]]:
            continue
        
        heapq.heappush(heap, (i[0], i[1]))

print(sum_w)