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

N = int(input())  # N: 컴퓨터의 수
M = int(input())  # M: 선의 수
heap = []
for _ in range(M):
    a, b, c = map(int, input().split())  # 가중치 오름차순으로 저장
    heappush(heap, (c, a, b))
parent = [i for i in range(N+1)]
cost = 0 # 최소 스패닝 트리의 가중치를 저장할 변수, 초기값 0
while heap:
    c, a, b = heappop(heap)  # pop
    if find(a) != find(b):
        union(a, b)
        cost += c
print(cost)  # 출력