import heapq
import sys
input = sys.stdin.readline


# def prim(start):
#     heap = []
#     MST = [0]*(V+1)
#     heapq.heappush(heap, (0, start))
#     sum_weight = 0
#     while heap:
#         weight, v = heapq.heappop(heap)
#         if MST[v]:
#             continue
#         MST[v] = 1
#         sum_weight += weight
#         for next in graph[v]:
#             if not MST[next[0]]:
#                 heapq.heappush(heap, (next[1], next[0]))
#     return sum_weight
#
#
# V = int(input())
# E = int(input())
# graph = [[] for _ in range(V+1)]
# for _ in range(E):
#     f, t, w = map(int, input().split())
#     graph[f].append([t, w])
#     graph[t].append([f, w])
# print(prim(1))


# # Kruskal
# V = int(input())
# E = int(input())
# graph = []
# for _ in range(E):
#     f, t, w = map(int, input().split())
#     graph.append([f, t, w])
# graph.sort(key=lambda x: x[2])
#
# parents = [i for i in range(V+1)]
#
# def find_set(x):
#     if parents[x] == x:
#         return x
#     return find_set(parents[x])
#
#
# def union(x, y):
#     x = find_set(x)
#     y = find_set(y)
#
#     if x == y:
#         return
#
#     if x < y:
#         parents[y] = x
#     else:
#         parents[x] = y
#
# cnt = 0
# sum_weight = 0
# for f, t, w in graph:
#     if find_set(f) != find_set(t):
#         cnt += 1
#         sum_weight += w
#         union(f, t)
#         if cnt == V:
#             break
# print(sum_weight)