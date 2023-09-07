def bfs(i,j):
    q = []
    q.append((i,j))
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    snake = []
    while q:
        i,j = q.pop(0)
        snake.append((i,j))
        ni,nj = i,j+1
        for a in turn:
            if cnt >= a[0]:
                if a[1] = 'L':
                    ni,nj = i+1,j
                else:


N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
turn = []
for _ in range(K):
    i,j = map(int,input().split())
    arr[i][j] = 1
    arr[j][i] = 1
L = int(input())
for _ in range(L):
    a,b = input().split()
    turn.append([int(a),b])
print(turn)