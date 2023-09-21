# 서로소 집합을 활용한 kruskal 알고리즘 활용

# 대표차 찾기
def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

# 대표자 저장 과정 (루트의 동일 여부로 판단)
def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x<y:
        parents[y] = x
    else:
        parents[x] = y

V,E = map(int,input().split())
edge = []
for _ in range(E):
    a,b,c = map(int,input().split())
    edge.append([a,b,c])
# 가중치를 기준으로 오름차순정렬
edge.sort(key=lambda x:x[2])

# make set 과정
parents = [i for i in range(V+1)]

# 정점 방문 횟수 기록
cnt = 0
# 지나온 간선의 가중치 기록
suma = 0
# 찾을 수 있는 모든 최소 신장 트리의 경우의 수 찾기
for a,b,c, in edge:
    # 싸이클이 발생하지 않을때마다 실행
    if find_set(a) != find_set(b):
        cnt += 1
        suma += c
        union(a,b)
        # 최소 신장 트리를 구하면
        if cnt == V:
            break
print(suma)