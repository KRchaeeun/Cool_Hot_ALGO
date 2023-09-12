import sys
input = sys.stdin.readline

def dfs(x, y):
    stack = [(x, y)]
    s[x][y] = '.'

    while stack:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<H and 0<=ny<W and s[nx][ny] == '#':
                s[nx][ny] = '.'
                stack.append((x, y))
                x = nx
                y = ny
                break
        else:
            x, y = stack.pop()

    return 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input().rstrip())

for _ in range(T):
    H, W = map(int, input().rstrip().split())
    s = [list(input().rstrip()) for _ in range(H)]
    ans = 0

    for x in range(H):
        for y in range(W):
            if s[x][y] == '#':
                ans += dfs(x, y)

    print(ans)