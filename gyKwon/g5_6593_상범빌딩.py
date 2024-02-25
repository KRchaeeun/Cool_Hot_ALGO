import sys
from collections import deque

move = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]

def bfs(x,y,z):
    global move
    q = deque()
    q.append((x,y,z))
    visited[x][y][z] = 1


    while q:
        a,b,d = q.popleft()
        if arr[a][b][d] == "E":
            return f"Escaped in {visited[a][b][d]-1} minute(s)."
        for da,db,dd in move:
            na,nb,nd = a+da,b+db,d+dd
            if 0<=na<l and 0<=nb<r and 0<=nd<c and not visited[na][nb][nd] and (arr[na][nb][nd] == "." or arr[na][nb][nd] == "E"):
                q.append((na,nb,nd))
                visited[na][nb][nd] = visited[a][b][d] + 1

    return "Trapped!"


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    arr = []
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    for k in range(l):
        arr.append([list(input().rstrip()) for _ in range(r)])
        input()

    for x in range(l):
        for y in range(r):
            for z in range(c):
                if arr[x][y][z] == "S":
                    print(bfs(x,y,z))



