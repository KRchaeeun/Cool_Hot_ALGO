import sys
sys.stdin = open("input.txt")

# 정점의 수 N, 간선의 수 M, 시작 정점 R을 입력받는다.
N, M, R = map(int, input().split())

# 그래프를 표현할 인접 리스트 초기화
graph = [[] for _ in range(N+1)]

# 주어진 간선을 양방향으로 인접 리스트에 추가하자.
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 각 정점의 인접 리스트를 정렬(오름차순으로 방문하기 위함)
for i in range(1, N+1):
    graph[i].sort()

# 방문 여부 및 방문 순서를 저장할 리스트 초기화
visited = [0] * (N+1)

# 방문 순서
visited_order = 1

# 시작 노드를 스택에 넣어주자.
stack = [R]

while stack:
    node = stack.pop()

    # 아직 방문하지 않은 노드일 경우
    if not visited[node]:
        visited[node] = visited_order
        visited_order += 1

        # 현재 노드와 연결된 노드들 중 방문하지 않은 노드를 스택에 추가
        for adj in reversed(graph[node]):  # 스택이므로 높은 번호부터 추가 (LIFO)
            if not visited[adj]:
                stack.append(adj)

for i in range(1, N+1):
    print(visited[i])