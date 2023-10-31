r, c, t = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치 찾기
air1 = 0
air2 = 0
for i in range(r):
    if dust[i][0] == -1:
        air1 = i
        air2 = i+1
        break

# 먼지 확산
def f1():
    di = [-1, 0, 0, 1]
    dj = [0, -1, 1, 0]

    arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            # 0이면 빈곳, -1이면 공기청정기가 위치한 곳
            if dust[i][j] != 0 and dust[i][j] != -1:
                a = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    # 밖으로 벗어나지 않고 공기청정기가 아닌 곳
                    if 0 <= ni < r and 0 <= nj < c and dust[ni][nj] != -1:
                        arr[ni][nj] += dust[i][j] // 5
                        a += dust[i][j] // 5 # a를 구한 이유는 해당 위치에 먼지를 빼주기 위해서
                dust[i][j] -= a
    # 다 했으면 퍼진 먼지를 각각에 넣어줌
    for i in range(r):
        for j in range(c):
            dust[i][j] += arr[i][j]


def air_1():
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    direction = 0 # 방향
    before = 0 # 이전값
    i, j = air1, 1
    while True:
        ni = i + di[direction]
        nj = j + dj[direction]
        if i == air1 and j == 0:
            break
        # 벽에 부딪히면 방향 전환
        if ni < 0 or ni >= r or nj < 0 or nj >= c:
            direction += 1
            continue
        dust[i][j], before = before, dust[i][j]
        i = ni
        j = nj


def air_2():
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    direction = 0
    before = 0
    i, j = air2, 1
    while True:
        ni = i + di[direction]
        nj = j + dj[direction]
        if i == air2 and j == 0:
            break
        if ni < 0 or ni >= r or nj < 0 or nj >= c:
            direction += 1
            continue
        dust[i][j], before = before, dust[i][j]
        i = ni
        j = nj

# 횟수만큼 반복
for _ in range(t):
    f1()
    air_1()
    air_2()

# 결과값 더하기
res = 0
for i in range(r):
    for j in range(c):
        if dust[i][j] > 0:
            res += dust[i][j]

print(res)