import sys
input = sys.stdin.readline
import heapq

def prim(start):
    heap = []
    MST = [0] * (V+1)
    heapq.heappush(heap, (0, start))
    sum_weight = 0
    while heap:
        weight, v = heapq.heappop(heap)

        if MST[v]:
            continue
        MST[v] = 1
        sum_weight += weight
        for next in graph[v]:
            if not MST[next[0]]:
                heapq.heappush(heap, (next[1], next[0]))
    return sum_weight


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])
    graph[t].append([f, w])
print(prim(1))