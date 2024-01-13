import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    q = deque()
    q.append((hx, hy))
    while q:
        x, y = q.popleft()
        # 이동거리가 도착지점 안에 있을 경우 happy
        if abs(x-fx) + abs(y-fy) <= 1000:
            return 'happy'
        # 편의점 찾기
        # 방문 안한 편의점에서 1000m안에 있는 편의점이 있을 경우
        # q에 추가 계속 이동
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    visited[i] = 1
                    q.append((nx, ny))
    # 못가면 sad
    return 'sad'


t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    store = []
    for _ in range(n):
        x, y = map(int, input().split())
        store.append((x, y))
    fx, fy = map(int, input().split())
    visited = [0] * (n+1)
    ans = bfs()
    print(ans)