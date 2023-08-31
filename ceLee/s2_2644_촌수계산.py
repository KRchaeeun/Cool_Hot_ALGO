from collections import deque

def bfs(start, end):
    queue = deque([(start, 0)])  # 시작 노드와 현재까지의 거리(촌수)를 함께 저장
    visited = [0] * (n + 1)  # 방문 표시를 위한 리스트
    visited[start] = 1  # 처음 시작하는 번호 방문 표시
    while queue:  # 큐에 원소가 있을 때까지 while문 반복
        current, count = queue.popleft()  # pop(0)

        # 목표에 도달한 경우(종료문)
        if current == end:
            return count

        for neighbor in lst[current]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append((neighbor, count + 1))

    return -1  # queue가 빌 때까지 경로를 찾지 못한 경우

n = int(input())  # n: 전체 사람의 수
guess_x, guess_y = map(int, input().split())  # 촌수를 계산해야하는 서로 다른 두 사람의 번호
m = int(input())  # m: 부모 자식들 간의 관계의 개수
lst = [[] for _ in range(n + 1)]  # 부모자식간의 관계를 나타내는 정보를 저장 할 리스트
for _ in range(m):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)
# 출력
print(bfs(guess_x, guess_y))