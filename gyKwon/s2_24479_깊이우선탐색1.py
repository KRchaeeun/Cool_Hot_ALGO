import sys
input = sys.stdin.readline
# 재귀함수를 사용하기 위해 재 설정
sys.setrecursionlimit(1000000)
# 깊이 우선 탐색 함수 설정
def dfs(R):
    global cnt
    global visited
    stack = []
    stack.append(R)
    # 1 번 노드부터 탐색하기 때문에 cnt 초기값을 1로 설정
    visited[R] = cnt
    cnt += 1
    # 재귀함수-> 연결리스트는 오름차순으로 정렬되어있음
    # 오름차순으로 탐색하면서 방문하지 않았다면 해당 노드로 이동
    # 방문할 수 있는 노드가 존재할때까지(간선이 연결되어 있는 경우) 탐색
    # 간선이 연결되어 있지 않아 방문 할 수 없을 시 0 출력
    # 이 경우에는 노드가 5까지 있지만, 5로 연결된 간선이 없어서 0 출력
    for w in arr[R]:
        if visited[w] == 0:
            dfs(w)

N,M,R = map(int,input().split())
arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
# 메모리 초과를 고려하여 연결리스트로 받아주기
for _ in range(M):
    i,j = map(int,input().split())
    arr[i].append(j)
    arr[j].append(i)
# 오름차순으로 탐색하기 때문에 정렬
for k in range(N+1):
    arr[k].sort()

dfs(R)
# for a in range(1,N+1):
#     print(visited[a])
print(arr)