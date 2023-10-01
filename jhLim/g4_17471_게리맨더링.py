import sys, itertools, collections
input = sys.stdin.readline

# bfs
def bfs(start, area):
    qu = collections.deque()
    visited = [0] * N

    qu.append(start)
    visited[start] = 1

    while qu:
        start = qu.popleft()

        for i in area:
            if (i in con[start]) and visited[i] == 0:
                qu.append(i)
                visited[i] = 1

    for j in area:
        if visited[j] == 0:
            return False

    return True


# input, 마을번호 임의로 0~N-1까지로 설정
N = int(input().rstrip())
num = list(map(int, input().rstrip().split()))
ans = set()

# 구역 잇기
con = [[]*(N) for _ in range(N)]

for i in range(N):
    lst = list(map(int, input().rstrip().split()))

    for j in range(1, lst[0]+1):
        con[i].append(lst[j]-1)

# 구역을 2개씩 나누기
for i in range(1, N//2+1):
    area1 = list(itertools.combinations(range(N), i))
    area2 = []

    for j in range(len(area1)):
        x = []
        for k in range(N):
            if k not in area1[j]:
                x.append(k)
        area2.append(x)

    # 나눈 구역이 서로 연결되었는지 확인
    for l in range(len(area1)):
        cnt1 = 0
        cnt2 = 0
        
        # 나눈 구역끼리 연결되어있다면 각 지역 인구의 합을 구하고 뺌
        if bfs(area1[l][0], area1[l]) and bfs(area2[l][0], area2[l]):
            for m in area1[l]:
                cnt1 += num[m]
            for n in area2[l]:
                cnt2 += num[n]
            ans.add(abs(cnt1-cnt2))

if ans:
    print(min(ans))
else:
    print(-1)