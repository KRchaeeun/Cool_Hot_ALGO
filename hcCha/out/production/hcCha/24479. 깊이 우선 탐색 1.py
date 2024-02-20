import sys
input = sys.stdin.readline


def dfs(start, vertex, adj_m):
    # 지나온 길을 기록하기 위한 스택
    stack = [0]

    # 방문했던 길인지 기록하기위한 리스트 0 또는 1로 확인
    visit = [0] * (vertex + 1)

    # 출발지점 n으로 설정하고 방문기록을 남긴다.
    n = start
    visit[n] = 1
    print(n)

    # 스택이 비어있지 않다면 반복한다.
    while stack:
        # 갈 수 있는 점은 1부터 vertex 까지
        for w in range(1, vertex + 1):
            # 간선이 1인경우, 즉 간선으로 이어져 있고 / 방문기록이 0인 경우
            if w in adj_m[n] and not visit[w]:
                # 스택에 현 지점을 넣고
                stack.append(n)
                # 이동하고
                n = w
                # 도착한 지점을 방문기록하고
                visit[n] = 1
                print(n)
                break
        # 더이상 갈 수 없는 경우 지나온길을 되짚어보기 위해 top으로 현재지점을 바꾸고 삭제
        else:
            n = stack.pop()
    # 길이 없다면 0출력
    return print(0)


# 정점, 간선, 시작점
Vertex, Edge, Start = map(int, input().split())

# # 간선 정보를 2차원 배열로 받는다.
# edge_info = [list(map(int, input().split())) for _ in range(Edge)]

# 간선정보를 입력한 행렬
adj_m = [[] for _ in range(Vertex + 1)]
for _ in range(Edge):
    u, v = map(int, input().split())
    adj_m[u] += [v]

dfs(Start, Vertex, adj_m)
