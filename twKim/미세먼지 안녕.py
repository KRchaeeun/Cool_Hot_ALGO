import sys
input = sys.stdin.readline

def diffusion(matrix1):
    dust = []
    for i in range(R):
        for j in range(C):
            if matrix1[i][j]:
                if matrix1[i][j] != -1:
                    dust.append([i, j, matrix1[i][j]])
    matrix1 = [[0]*C for _ in range(R)]
    matrix1[clean_up[0]][0] = -1
    matrix1[clean_down[0]][0] = -1
    for i in dust:
        diffusion_dust = i[2] // 5
        matrix1[i[0]][i[1]] += i[2]
        for j in range(4):

            nx = i[0] + delta[j][0]
            ny = i[1] + delta[j][1]

            if 0 <= nx < R and 0 <= ny < C and matrix1[nx][ny] != -1:
                matrix1[i[0]][i[1]] -= diffusion_dust
                matrix1[nx][ny] += diffusion_dust
    return matrix1


def cleanup():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = clean_up[0], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == clean_up[0] and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        matrix1[x][y], before = before, matrix1[x][y]
        x = nx
        y = ny
        

def cleandown():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = clean_down[0], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == clean_down[0] and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        matrix1[x][y], before = before, matrix1[x][y]
        x = nx
        y = ny


R, C, T = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(R)]
delta = ((0, 1), (1, 0), (-1, 0), (0, -1))
clean_up = []
clean_down = []
for i in range(R):
    for j in range(C):
        if matrix1[i][j]:
            if matrix1[i][j] == -1:
                if clean_up:
                    clean_down = [i, j, matrix1[i][j]]
                else:
                    clean_up = [i, j, matrix1[i][j]]

for i in range(T):
    matrix1 = diffusion(matrix1)
    cleanup()
    cleandown()

dust_sum = 0
for i in range(R):
    for j in range(C):
        if matrix1[i][j] and matrix1[i][j] != -1:
            dust_sum += matrix1[i][j]

print(dust_sum)