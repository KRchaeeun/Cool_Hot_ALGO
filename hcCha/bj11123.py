def dfs(n):
    for w in gp[n]:
        if not visited[w]:
            dfs(w)


T = int(input())
for tc in range(1, T + 1):
    row, col = map(int, input().split())
    matrix = [list(input()) for _ in range(row)]
    cnt_maeeeee = 0

    gp = [[] for _ in range(row + 1)]

    visited = [0] * (col + 1)

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '#':
                gp[i].append(j)

    dfs(0)