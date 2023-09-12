import sys
input = sys.stdin.readline

def dfs(start, end, n, arr):
    visited = [0] * (n+1)
    stack = []
    cnt = 0

    visited[start] = 1
    stack.append(start)

    while stack:
        if start == end:
            return cnt

        for i in range(1, n+1):
            if arr[start][i] == 1 and visited[i] == 0:
                visited[i] = 1
                stack.append(start)
                start = i
                cnt += 1
                break
        else:
            start = stack.pop()
            cnt -= 1

    return -1


n = int(input().rstrip())
x, y = map(int, input().rstrip().split())
m = int(input().rstrip())
arr = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().rstrip().split())
    arr[i][j] = 1
    arr[j][i] = 1

print(dfs(x, y, n, arr))