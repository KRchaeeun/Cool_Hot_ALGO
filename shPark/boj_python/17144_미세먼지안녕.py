"""
import sys
input = sys.stdin.readline


def find_air_cleaner():
    for i in range(R):
        for j in range(C):
            if house_wind[i][j] == -1:
                air_cleaner.append([i,j])
            if len(air_cleaner) == 2:
                return
            

def wind(x, y, order):
    dx, dy = delta_wind[order][0]
    x += dx
    y += dy
    for _ in range(R-1):
        if 0<=x+dx<R and 0<=y+dy<C:
            house_wind[x+dx][y+dy] = house_dirt[x][y]
            house_wind[x][y] = 0
            x += dx
            y += dy
        else:
            tmp = house_dirt[x][y]

    if y == 0 or y == C-1:
        return
    
    dx, dy = delta_wind[order][1]
    while 1:
        if 0<=x+dx<R and 0<=y+dy<C:
            house_wind[x+dx][y+dy] = tmp
            house_wind[x][y] = 0
            tmp = house_dirt[x+dx][y+dy]
            x += dx
            y += dy
        else:
            break

    dx, dy = delta_wind[order][2]
    for _ in range(R-1):
        if 0<=x+dx<R and 0<=y+dy<C:
            house_wind[x+dx][y+dy] = tmp
            tmp = house_dirt[x][y]
            x += dx
            y += dy
    
    dx, dy = delta_wind[order][3]
    while 1:
        if house_wind[x+dx][y+dy] != -1:
            house_wind[x+dx][y+dy] = tmp
            house_wind[x][y] = 0
            tmp = house_dirt[x][y]
            x += dx
            y += dy
        else:
            break


def sync():
    for i in range(R):
        for j in range(C):
            house_wind[i][j] = house_dirt[i][j]


def dirt():
    for i in range(R):
        for j in range(C):
            if house_wind[i][j] > 4:
                tmp = house_wind[i][j]
                cnt = 0
                for di, dj in delta:
                    ni = i + di
                    nj = j + dj
                    if 0<=ni<R and 0<=nj<C and house_dirt[ni][nj] != -1:
                        house_dirt[ni][nj] += tmp//5
                        cnt += 1
                house_dirt[i][j] += tmp - (cnt * (tmp//5))
            elif house_wind[i][j] != -1:
                house_dirt[i][j] += house_wind[i][j]


R, C, T = map(int, input().split())
house_wind = [list(map(int, input().split())) for _ in range(R)]
house_dirt = [[0]*C for _ in range(R)]

air_cleaner = []
find_air_cleaner()
for i, j in air_cleaner: house_dirt[i][j] = -1

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
delta_wind = [[[0, 1], [-1, 0], [0, -1], [1, 0]], [[0, 1], [1, 0], [0, -1], [-1, 0]]]
for cnt in range(T):
    dirt()
    sync()
    # for i in house_dirt:
    #     print(i)
    for order, axis in enumerate(air_cleaner):
        wind(axis[0], axis[1], order)

    for i in house_dirt:
        print(i)

    print()

    for i in house_wind:
        print(i)
    print()

    if cnt < T-2:
        house_dirt = [[0]*C for _ in range(R)]
        for i, j in air_cleaner: house_dirt[i][j] = -1

res = 0
for i in house_dirt:
    res += sum(i)

print(res+2)
"""

import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1

for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break


def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j]


def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny


def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0
for i in arr:
    answer += sum(i)

print(answer + 2)