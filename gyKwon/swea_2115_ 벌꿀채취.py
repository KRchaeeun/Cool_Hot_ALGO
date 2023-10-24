### 미완성

from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited = [[0]*(N) for _ in range(N)]
    visited[i][j] = 1
    suma = []
    while q:
        i,j = q.popleft()
        for z in range(1,M):
            nj = j+z
            if 0<= nj <N and visited[i][nj] == 0:
                q.append((i,nj))
                visited[i][nj] = 1
                suma.append(arr[i][nj])

    return suma, visited

def chs(k):
    global ssa
    global klis
    global finlis

    if sum(klis)<=C and sum(klis)>ssa:
        ssa = sum(klis)
        finlis = klis
        return
    for i in range(len(k)):
        if k[i] not in klis:
            klis.append(k[i])
            chs(k)
            klis.pop()

ssa = -10e9
klis = []
finlis = []

def wheres():
    global ssa
    for x in range(N):
        for y in range(N-M+1):
            sumxy = 0
            k,visa = bfs(x,y)
            if sum(k)<=C:
                for p in k:
                    sumxy += p**2

            else:
                chs(k)
                for u in finlis:
                    sumxy += u**2
                ssa = -10e9
                klis = []
                finlis = []

            sumxy2 = []
            for n in range(N):
                for m in range(N-M+1):
                    if visa[n][m] ==0 and visa[n][m+M-1] and 0<=m<N and 0<=m+M-1<N:
                        k2,visa2 = bfs(n,m)

                        if sum(k2) <= C:
                            for p2 in k2:
                                sumxy2.append(p2 ** 2)
                        else:
                            chs(k2)
                            for u2 in klis:
                                sumxy2.append(u2 ** 2)
                            ssa = -10e9
                            klis = []
                            finlis = []

            fina.append(sumxy+max(sumxy2))

T = int(input())
for tc in range(1,T+1):
    N,M,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    fina = []
    wheres()
    print(f'#{tc} {max(fina)}')