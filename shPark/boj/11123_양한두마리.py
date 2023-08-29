# BOJ_11123 : 양 한마리... 양 두마리 ...
import sys
from collections import deque

# input = sys.stdin.readline
sys.stdin = open('input.txt')


# bfs 방식으로 양 탐색
def find_sheep(x, y):
    q = deque()
    q.append([x, y])
    while q:
        nx, ny = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = nx + di, ny + dj
            if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and fld[ni][nj] == '#':
                # 거리가 필요한게 아니니까 전부 1처리
                visited[ni][nj] = 1
                q.append([ni, nj])

    # 함수가 몇번 호출됐는지가 중요하니까 return 1
    return 1


"""
점과 양으로만 이루어진 필드
상하좌우로 붙어있다면 하나의 무리로 본다
음 그럼 어쩌지
# 이 존재할 때만 탐색
주위로 퍼져나가면서 탐색하면 되겠네
표시는 밖에다가 처리해야곘네
return 은 cnt 만 해주고
for 문을 순회하며 모든 값에 대해서 탐색
함수 내부에서는 순회하면서 visited 만 처리
"""

T = int(input())
for _ in range(T):
    h, w = map(int, input().rstrip().split())
    fld = [list(input().rstrip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    res = 0
    # 모든 곳을 탐색하면서 진행
    for i in range(h):
        for j in range(w):
            # 양을 찾았고 이전에 발견된 곳이 아닐때만 함수 호출
            if fld[i][j] == '#' and visited[i][j] == 0:
                res += find_sheep(i, j)
    print(res)
