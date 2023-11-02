r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
front = 0
back = 0


for i in range(r) :
    if room[i][0] == -1 :
        front = i
        back = i + 1
        break

def spread() :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    temp = [[0] * c for _ in range(r)]
    for i in range(r) :
        for j in range(c) :
            if room[i][j] != 0 and room[i][j] != -1 :
                value = 0
                for k in range(4) :
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1 :
                        temp[nx][ny] += room[i][j] // 5
                        value += room[i][j] // 5
                room[i][j] -= value
    for i in range(r) :
        for j in range(c) :
            room[i][j] += temp[i][j]


def airup():

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = front, 1
    while True :
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == front and y == 0 :
            break
        if not 0 <= nx < r or not 0 <= ny < c :
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x, y = nx, ny


def airdown() :
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = back, 1
    while True :
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == back and y == 0 :
            break
        if not 0 <= nx < r or not 0 <= ny < c :
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x, y = nx, ny

for _ in range(t) :
    spread()
    airup()
    airdown()

result = 0
for i in range(r) :
    for j in range(c) :
        if room[i][j] > 0 :
            result += room[i][j]

print(result)