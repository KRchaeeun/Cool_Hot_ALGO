import sys

input = sys.stdin.readline


def dfs(x, y, num, m, T_F):                 # 그래프 탐색
                                            # T_F는 글씨를 바꾸겠다는걸 표시
    global max_num                          # max 넣어줄거

    if not (x_k == x or y_k == y):          # 델타 벗어나면 return
        return

    for i in range(4):                      # 4방향 탐색

        nx = x + delta[i][0]
        ny = y + delta[i][1]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:

            if matrix[nx][ny] == m and T_F == 0:        # 만약 글자가 같다면 방문 기록 남기고
                visited[nx][ny] = 1
                dfs(nx, ny, num + 1, m, 0)              # 갯수를 하나 세주고 다음 칸으로 간다.
                visited[nx][ny] = 0                     # 돌아오면 방문한 기록을 없애줌

            elif matrix[nx][ny] == m and matrix[x][y] != m and T_F == 1:    # 다음 글자가 처음 들어온 글자랑 같고
                                                                            # 지금 내 글자는 다른 글자라면
                matrix[x][y], matrix[nx][ny] = matrix[nx][ny], matrix[x][y] # 두개의 칸을 바꾸고
                dfs(x, y, num + 1, m, 1)                                    # 다음 칸으로 진행
                matrix[x][y], matrix[nx][ny] = matrix[nx][ny], matrix[x][y] # 다시 원상복귀

            elif matrix[nx][ny] == m and T_F == 1:                          # 다음 글자가 같으면 처음 위치랑 같으면
                visited[nx][ny] = 1
                dfs(nx, ny, num + 1, m, 1)                                  # 다음칸으로 전진
                visited[nx][ny] = 0

            elif matrix[nx][ny] != m and T_F == 0:                          # 칸이 다르면
                visited[nx][ny] = 1
                dfs(nx, ny, num, m, 1)                                      # 일단은 전진하고 바꾸기 권을 쓰겠다는 의미로
                                                                            # T_F를 1로 만들어줌
                visited[nx][ny] = 0
    else:
        if max_num < num:                                                   # max 갱신
            max_num = num
        return


N = int(input())
max_num = 0
matrix = [list(input().strip()) for _ in range(N)]
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        visited[i][j] = 1
        x_k, y_k = i, j
        dfs(i, j, 1, matrix[i][j], 0)
        visited[i][j] = 0

print(max_num)