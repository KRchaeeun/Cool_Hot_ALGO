from collections import deque
from itertools import combinations

def bfs(lst):
    start = lst[0]
    visited = [0] * (cnt_city + 1)
    q = deque([start])
    cnt = 0
    visited[start] = 1
    while q:
        x = q.popleft()
        cnt += 1
        for i in graph[x]:
            # 내 선거구에 포함된 도시인지 확인
            if visited[i] == 0 and i in lst:
                visited[i] = 1
                q.append(i)
    # 내 선거구에 포함되고 연결된 도시의 갯수 확인
    return cnt

# 도시의 개수
cnt_city = int(input())
# 도시당 사람 수
people_city = [0] + list(map(int, input().split()))
# 그래프 생성
graph = [0]
for _ in range(cnt_city):
    temp = list(map(int, input().split()))
    # 맨 앞에 갯수 제거하고 담기
    graph.append(temp[1::])

# 최종 인구수 차 리스트
rst = []
# 조합이기 때문에 모든 도시 갯수의 절반만 구해도 나머지 절반은 구할 수 있음
for i in range(1, (cnt_city//2) + 1):
    # combinations 함수로 i개의 도시를 가진 조합 생성
    temp = list(combinations(range(1, cnt_city + 1), i))
    # 각 조합을 하나씩 살펴보자.
    for a in temp:
        # 반대 조합을 담을 리스트
        b = []
        for n in range(1, cnt_city + 1):
            if n in a:
                continue
            b.append(n)

        # 반환받은 연결된 도시의 갯수의 합 == 총 도시의 갯수와 같다면 / 두 선거구로 나눌 수 있다.
        if bfs(a) + bfs(b) == cnt_city:
            # 각 선거구 도시의 인구 차를 구해서 최종 리스트에 담는다.
            ap = bp = 0
            for city in range(1, cnt_city + 1):
                if city in a:
                    ap += people_city[city]
                else:
                    bp += people_city[city]
            rst.append(abs(ap - bp))

# 비어있다면 -1 아니라면 최솟값
if rst:
    print(min(rst))
else:
    print(-1)



