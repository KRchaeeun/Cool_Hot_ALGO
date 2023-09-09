**************미완성

def bfs(i,j):
    global di,dj
    q = []
    q.append((i,j))
    visited = [[0]*N for _ in range(N)]

    while True:
        i,j = q.pop(0)
        mv = 1
        ni = i+di[mv%4]
        nj = j+dj[mv%4]
        if ni>N and ni<0 and nj>N and nj<0 and (ni,nj) in q:
            break
        for


N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
turn = []
for _ in range(K):
    i,j = map(int,input().split())
    arr[i-1][j-1] = 1
L = int(input())
for _ in range(L):
    a,b = input().split()
    turn.append([int(a),b])
di = [-1,0,1,0]
dj = [0,1,0,-1]
