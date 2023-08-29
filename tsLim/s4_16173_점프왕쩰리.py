import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(i, j):
    # 밖으로 벗어나거나 이미 방문하였을 경우
    if i<0 or i>=N or j<0 or j>=N or visited[i][j] == 1:
        return

    # 도착지는 -1로 되어있기 때문에 맞다면 방문확인후 함수 종료
    if arr[i][j] == -1:
        visited[i][j] = 1
        return

    # 방문 확인 후 오른쪽, 아래쪽으로 다시 함수 호출
    visited[i][j] = 1
    dfs(i+arr[i][j], j)
    dfs(i, j+arr[i][j])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dfs(0, 0)

# 방문 목록의 마지막위치가 1로 되어있다면
if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')

