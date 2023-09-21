import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def prim(start):
    heap = []
    mst = [0] * (V+1)

    heappush(heap, (0, start))
    cnt = 0

    while heap:
        c, v = heappop(heap)

        if mst[v]:
            continue

        mst[v] = 1
        cnt += c

        for n, nc in trees[v]:
            if mst[n]:
                continue
            heappush(heap, (nc, n))
    
    return cnt


V, E = map(int, input().rstrip().split())
trees = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    trees[a].append((b, c))
    trees[b].append((a, c))

print(prim(1))