from collections import deque
# 델타 검색: 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(i, j):

    # stack: [x좌표, y좌표] 삽입할 리스트
    stack = deque([])
    stack.append([i, j])

    # BFS 시작
    while stack:  # stack이 빌때까지 while문 반복
        x, y = stack.popleft()  # stack 저장되어있는 x좌표와 y좌표를 pop하고 x, y에 저장

        for d in range(4):  # 델타 검색 총 4개
            nx = x + di[d]
            ny = y + dj[d]
            if 0 <= nx < H and 0 <= ny < W and field[nx][ny]:  # nx, ny가 배열을 넘지 않고 field가 1일때 (방문하지 않았거나 풀이지 않을때)
                field[nx][ny] = 0  # 방문 표시로 0으로 바꾸어주고
                stack.append([nx, ny])  # 이 점에서 델타 탐색을 해야하므로 x좌표와 y좌표를 stack에 저장

T = int(input())  # T: 테스트 케이스 개수
for _ in range(1, T + 1):
    H, W = map(int, input().split())

    field = []  # filed: 초원의 양과 풀을 숫자로 저장할 리스트
    for _ in range(H):
        lst = input()  # lst: input값 받기
        row = []  # 각 input값의 양과 초원을 숫자로 저장하기 위한 리스트
        for elem in lst:  # lst에 있는 원소(# or .)
            if elem == '#':  # 만약 #이면 (양이면)
                row.append(1)  # 1로 저장
            else:  # . 이면 (초원이면)
                row.append(0)  # 0으로 저장
        field.append(row)  # [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1]]

    cnt = 0  # cnt: 양무리의 개수를 저장할 변수, 초기값 0

    for i in range(H):
        for j in range(W):
            if field[i][j]:  # 양이면 (1)
                field[i][j] = 0  # 방문 표시로 0으로 바꾸고
                BFS(i, j)  # BFS 시작
                cnt += 1  # BFS 돌때마다 cnt +1

    print(cnt)  # 출력