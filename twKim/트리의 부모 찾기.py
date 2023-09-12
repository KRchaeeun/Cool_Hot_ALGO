import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
Tree = [[] for i in range(N + 1)]
Tree_p = [0]*(N+1)
q = deque([1])
Tree_p[1] = 1           # 1의 부모는 사실상 없으니 자기 자신으로 지정
for i in range(N-1):    # 입력 받아오기
    a, b = map(int, input().split())
    Tree[a].append(b)   # 양면으로 입력 해줌
    Tree[b].append(a)   # 얘도 양면으로 입력 해줌

while q:
    current_node = q.popleft()          # 현재 노드에 q를 뽑아옴

    for i in Tree[current_node]:        # 현재 노드를 i에 넣어서
        if not Tree_p[i]:
            Tree_p[i] = current_node    # 트리에 부모가 없으면 얘를 부모로 지정해줌
            q.append(i)                 # bfs를 돌리기 위해 append해줌

for i in range(2,N+1):
    print(Tree_p[i])                    # print해줌