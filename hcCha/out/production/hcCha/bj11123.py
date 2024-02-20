def dfs(x, y):
    global cnt_maeeeee
    matrix[x][y] = '.'
    for k in range(4):
        ni, nj = x + di[k], y + dj[k]
        if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] == '#':
            dfs(ni, nj)


T = int(input())
for tc in range(1, T + 1):
    row, col = map(int, input().split())
    matrix = [list(input()) for _ in range(row)]
    cnt_maeeeee = 0

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '#':
                dfs(i, j)
                cnt_maeeeee += 1

    print(cnt_maeeeee)
