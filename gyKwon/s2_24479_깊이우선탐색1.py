########메모리 초과!!!!!##############

def dfs(N,rdmap,I):
    stack = []
    visited = [0]*(N+1)
    visited[I] = 1
    print(I)
    while True:

        for w in range(1,N+1):
            if rdmap[I][w] == 1 and visited[w] == 0:
                stack.append(I)
                I = w
                print(I)
                visited[I] = 1
                break
        else:
            if stack:
                I = stack.pop()
            else:
                print(0)
                break
    return


N,M,I = list(map(int,input().split()))
road = []
for _ in range(N):
    s,g = list(map(int,input().split()))
    road.append(s)
    road.append(g)
rdmap = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    v1,v2 = road[i*2], road[i*2+1]
    rdmap[v1][v2] = 1
    rdmap[v2][v1] = 1

dfs(N,rdmap,I)