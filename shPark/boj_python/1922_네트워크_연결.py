import heapq
import sys

sys.stdin = open('input.txt')
# input = sys.stdin.readline


def prim():
    q = []
    mst = [0] * (V+1)
    # 1번노드부터 시작
    heapq.heappush(q, (0, 1))

    weights = 0
    while q:
        weight, now = heapq.heappop(q)
        
        # 방문한적 있으면 넘김
        if mst[now]:
            continue
        
        # 방문처리
        mst[now] = 1
        # 가중치 추가
        weights += weight

        for info in gp[now]:
            # 방문한 적 있으면 넘김
            if mst[info[1]]:
                continue
            heapq.heappush(q, (info[0], info[1]))
    return weights


# 프림으로 다시구현
V = int(input())
E = int(input())

gp = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    gp[u].append([w, v])
    gp[v].append([w, u])

print(prim())
