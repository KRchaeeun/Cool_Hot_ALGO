from collections import deque


def bfs(s, graph, visited, clink):
    q = deque([s])
    visited[s] = 1
    cnt = 1
    while q:
        s = q.popleft()
        for w in graph[s]:
            if visited[w] == 0 and clink[s][w]:
                q.append(w)
                visited[w] = 1
                cnt += 1
    return cnt


def solution(n, wires):
    answer = 10e9

    clink = [[1] * (n + 1) for _ in range(n + 1)]

    graph = [[] for _ in range(n + 1)]
    cnt_all = []

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [0] * (n + 1)

        clink[a][b] = 0
        cnta = bfs(a, graph, visited, clink)
        cntb = bfs(b, graph, visited, clink)
        clink[a][b] = 1

        answer = min(answer, abs(cnta - cntb))

    return answer

# 망한 코드
# from itertools import combinations
# from collections import deque

# def solution(n, wires):
#     answer = -1
#     def bfs(lst):
#         q = deque()
#         st = lst[0]
#         q.append(st)
#         visited = [st]
#         while q:
#             s = q.popleft()
#             for w in arr[s]:
#                 if w not in visited and w in lst:
#                     q.append(w)
#                     visited.append(w)
#         return visited

#     arr = [[] for _ in range(n+1)]
#     for wire in wires:
#         a,b = wire[0],wire[1]
#         arr[a].append(b)
#         arr[b].append(a)

#     finlis = []
#     for i in range(1, n//2+1):
#         comlis = list(combinations(range(1,n+1),i))
#         for cs in comlis:
#             c1 = bfs(cs)
#             cs2 = []
#             for i in range(1,n+1):
#                 if i not in cs:
#                     cs2.append(i)
#             c2 = bfs(cs2)

#             f1 = 0
#             for k in c1:
#                 if k not in cs:
#                     f1 = 0
#                     break
#                 else:
#                     f1 = 1
#             f2 = 0
#             for j in c2:
#                 if j not in cs2:
#                     f2 = 0
#                     break
#                 else:
#                     f2 = 1

#             if f1+f2 == 2:
#                 finlis.append(abs(len(cs)-len(cs2)))
#     answer = min(finlis)


#     return answer