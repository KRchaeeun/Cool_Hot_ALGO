# 대표자 찾기
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

# 대표 합치기
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 크루스칼 알고리즘
def kruskal():
    cnt, rst = 0, 0
    for w, f, t in edge:
        # 대표가 다른경우 / 다른 집합인 경우 / 이어지지 않은 경우
        if find_set(f) != find_set(t):
            # 추가된 간선 + 1
            cnt += 1
            # 비용 합
            rst += w
            # 대표 합치기 / 연결하기
            union(f, t)
            # 간선의 수 (노드번호 -1) 인 경우 / 모든 간선 연결한 경우
            if cnt == V - 1:
                return rst


V = int(input())
E = int(input())

edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append((w, f, t))

# 비용 기준 정렬
edge.sort()

# 대표확인 리스트/ 집합 구분 리스트 / 디스조인셋 알고리즘 리스트
parents = [i for i in range(V + 1)]

print(kruskal())
