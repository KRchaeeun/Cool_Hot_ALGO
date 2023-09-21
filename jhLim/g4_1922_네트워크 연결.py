from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def prim(start):
    heap = []
    mst = [0] * (N+1)

    heappush(heap, (0, start))
    cnt = 0

    while heap:
        cost, com = heappop(heap)

        if mst[com]:
            continue

        mst[com] = 1
        cnt += cost

        for ncom, ncost in computer[com]:
            if mst[ncom]:
                continue
            heappush(heap, (ncost, ncom))

    return cnt
            

N = int(input().rstrip())
M = int(input().rstrip())
computer = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    computer[a].append((b, c))
    computer[b].append((a, c))

print(prim(1))