import sys
from collections import deque


def game():
    q = deque()
    q.append((0, 0))
    # 시간
    sec = 0
    # 방향
    direction = 0
    while 1:
        # 시간 측정
        sec += 1
        # 방향 도출
        x, y = direc[direction]
        # 뱀의 머리 위치
        nx, ny = q[0]
        # 진행방향
        dx, dy = x + nx, y + ny
        # 보드 밖으로 나가는지 검사
        if 0 <= dx < n and 0 <= dy < n:
            # 몸통에 부딫치는지 검사
            if (dx, dy) in q:
                # 부딫치면 시간 리턴
                return sec
            # 진행방향에 사과가 있다면
            if fld[dx][dy]:
                # 사과를 먹고
                fld[dx][dy] = 0
            # 없으면 꼬리칸을 한칸 줄인다
            else:
                q.pop()
            # 머리 append
            q.appendleft((dx, dy))

        # 밖으로 나가면 고대로 시간 리턴
        else:
            return sec
        
        # 현재 시간의 움직임이 끝난 후 머리를 돌린다 했으므로 마지막에 방향 체크
        # 만약 해당 시간에 머리를 돌린다는 정보가 있다면,
        if moving.get(sec, False):
            # 'D'는 시계방향으로 90도 회전
            if moving[sec] == 'D':
                direction += 1
            # 'L'은 반시계방향으로 90 도 회전
            else:
                direction -= 1
            # 4로 나눈 나머지로 인덱스 사용
            direction %= 4


# 방향을 시계방향으로 설정 90도 씩 움직인다 했으니까
# 최초의 방향은 오른쪽을 본다고 주워졌으니까
# 우, 하, 좌, 상
direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# input = sys.stdin.readline
n = int(input())
fld = [[0] * n for _ in range(n)]
apple = int(input())
# 사과의 위치를 표기
for _ in range(apple):
    u, v = map(int, input().split())
    fld[u - 1][v - 1] = 1
turn = int(input())
moving = {}
# 방향전환을 dictionary 형으로 저장
for _ in range(turn):
    inp = input().rstrip().split()
    moving[int(inp[0])] = inp[1]
res = game()
print(res)
