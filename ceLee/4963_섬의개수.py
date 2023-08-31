from collections import deque
# 델타 검색: 상 하 좌 우 + 대각선
di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

def BFS(i, j):
    stack = deque([])  # stack
    stack.append([i, j])  # stack에 처음 좌표를 [x좌표, y좌표]로 넣기
    while stack:  # stack이 비워지기 전까지 while문 반복
        x, y = stack.popleft()  # pop(0)
        for d in range(8):  # 델타 8방향 검색
            nx = x + di[d]
            ny = y + dj[d]
            if 0 <= nx < h and 0 <= ny < w and field[nx][ny]:  # 배열을 벗어나지 않고 0이 아닌곳만 갈 수 있음
                field[nx][ny] = 0
                stack.append([nx, ny])  # 이 좌표에서 다시 확인을 해야하므로 stack에 저장

while True:
    w, h = map(int, input().split())  # w: 열의 길이, h: 행의 길이

    # 0,0이면 종료(종료 조건)
    if w == 0 and h == 0:
        break

    field = [list(map(int, input().split())) for _ in range(h)]  # 지도 정보 입력 받기

    cnt = 0  # 섬의 개수 셀 변수, 초기값 0

    for i in range(h):
        for j in range(w):
            if field[i][j]:
                field[i][j] = 0
                BFS(i, j)
                cnt += 1
    print(cnt)  # 출력