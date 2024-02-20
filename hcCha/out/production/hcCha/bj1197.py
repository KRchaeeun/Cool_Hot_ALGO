########################크루스칼 알고리즘##############
# 간선의 갯수가 적다면 크루스칼이 메모리와 속도가 빠르다

# 대표자 찾기
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

# 대표자 합치기
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())

# 간선 정보
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append((w, f - 1, t - 1))

# 정렬
edge.sort()

# 집합과 대표자 파악을 위한 리스트
parents = [i for i in range(V)]

cnt, rst = 0, 0
for w, f, t in edge:
    # 대표자가 다른 경우
    if find_set(f) != find_set(t):
        # 간선 연결
        cnt += 1
        rst += w
        union(f, t)
        # 간선 수만큼 진행시 브렠
        if cnt == V:
            break

print(rst)

################프림#####################
V, E = map(int, input().split())
import heapq
# 간선 정보
edge = [[] for _ in range(V)]
for _ in range(E):
    f, t, w = map(int, input().split())
    heapq.heappush(edge[f - 1], (w, t - 1))
    heapq.heappush(edge[t - 1], (w, f - 1))

visited = [0] * V
sum_v = 0
q = [(0, 0)]
while q:
    w, t = heapq.heappop(q)

    if visited[t]:
        continue

    sum_v += w
    visited[t] = 1

    for nw, nt in edge[t]:
        if visited[nt] == 0:
            heapq.heappush(q, (nw, nt))

print(sum_v)