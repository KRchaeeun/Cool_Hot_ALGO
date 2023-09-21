import sys
sys.stdin = open("input.txt")
from heapq import heappop, heappush

# 루트 노드를 찾는 함수
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])  # 압축
    return parent[x]

# 결합하는 함수
def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x

num_node, num_edge = map(int, input().split())  # num_node: 정점의 개수, num_edge: 간선의 개수
parent = [i for i in range(num_node+1)]
edges = []  # 간선의 정보를 저장할 리스트
for _ in range(num_edge):
    a, b, c = map(int, input().split())
    heappush(edges, (c, a, b))  # 가중치 오름차순으로 저장
weight_result = 0  # 최소 스패닝 트리의 가중치를 저장할 변수, 초기값 0
while edges:
    w, a, b = heappop(edges)  # pop
    if find(a) != find(b):
        union(a, b)
        weight_result += w
print(weight_result)  # 출력