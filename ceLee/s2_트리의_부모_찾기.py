def dfs(n):
    for i in tree[n]:
        if not visited[i]:
            visited[i] = n
            dfs(i)

n = int(input())  # n: 노드의 개수
visited = [0] * (n+1)  # 방문 표시겸 부모의 노드 번호
tree = [[] for _ in range(n+1)]  # 트리의 정보 입력
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)  # 트리의 루트 1, dfs호출해서 재귀 돌리기
# 출력
for i in range(2, n+1):
    print(visited[i])