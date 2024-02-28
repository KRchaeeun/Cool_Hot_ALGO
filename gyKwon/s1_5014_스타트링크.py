from collections import deque
import sys
input = sys.stdin.readline
def upndown(f,s,g,u,d):
    q = deque()
    q.append(s)
    visited = [0]*(f+1)
    visited[s] = 1
    while q:
        i = q.popleft()
        if i == g:
            return visited[g]-1
        for di in [u,-d]:
            ni = i + di
            if 1 <= ni <= f and not visited[ni]:
                visited[ni] = visited[i] + 1
                q.append(ni)
    return "use the stairs"

f,s,g,u,d = map(int,input().split())
fina = upndown(f,s,g,u,d)
print(fina)
