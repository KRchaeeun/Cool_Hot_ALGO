import sys
from collections import deque

sys.stdin = open('input.txt')
# input = sys.stdin.readline


# 촌수 찾는 함수, 중간에 조건에 합당하면 멈추는 bfs
def find_num(start_point, end_point):
    q = deque()
    q.append(start_point)
    visited[start_point] = 1
    while q:
        ppl_num = q.popleft()
        # 종료 조건
        if ppl_num == end_point:
            return visited[ppl_num] - 1

        for i in gp[ppl_num]:
            if not visited[i]:
                visited[i] = visited[ppl_num] + 1
                q.append(i)
    return -1


# 입력
n = int(input())
start_node, end_node = map(int, input().split())
e = int(input())

# 조건에 따른 변수
gp = [[] for _ in range(n+1)]
visited = [0] * (n+1)

# 가족관계 작성
for _ in range(e):
    par, chd = map(int, input().split())
    gp[par].append(chd)
    gp[chd].append(par)

# 함수 실행
res = find_num(start_node, end_node)
print(res)
