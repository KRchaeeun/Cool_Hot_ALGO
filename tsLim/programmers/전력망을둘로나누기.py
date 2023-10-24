from collections import deque


def bfs(start, visited, adj_l, link):
    q = deque([start])
    cnt = 1
    visited[start] = 1
    while q:
        x = q.popleft()
        for i in adj_l[x]:
            if not visited[i] and link[x][i] == 1:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt


def solution(n, wires):
    answer = 1e9
    adj_l = [[] for _ in range(n + 1)]
    link = [[1] * (n + 1) for _ in range(n + 1)]
    for a, b in wires:
        adj_l[a].append(b)
        adj_l[b].append(a)

    for a, b in wires:
        visited = [0] * (n + 1)
        link[a][b] = 0
        cnt_a = bfs(a, visited, adj_l, link)
        cnt_b = bfs(b, visited, adj_l, link)
        link[a][b] = 1
        answer = min(answer, abs(cnt_a - cnt_b))
    return answer