import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# 시간초과 남
'''
# 노드의 개수
cnt_node = int(input())
# 자식인덱스에 부모 노드 저장할 리스트
parents = [0] * (cnt_node + 1)
# 임시 보관
temp = deque([])
# 간선의 수 = 노드의 개수 - 1 만큼 저장
for _ in range(cnt_node - 1):
    i, j = map(int, input().split())
    # 입력값 중 1이 있다면 자식 인덱스에 1 저장
    if i == 1:
        parents[j] = i
    elif j == 1:
        parents[i] = j

    # 부모가 있는 노드가 입력값으로 주어진 경우 다른 입력값 인덱스에 부모 값 저장
    # i, j 모두 부모 값이 없는 경우 임시 보관
    if parents[i] != 0:
        parents[j] = i
    elif parents[j] != 0:
        parents[i] = j
    else:
        temp.append((i, j))

# 큐을 활용하여 하나씩 부모의 유무를 확인하고 위의 과정 진행
while temp:
    i, j = temp.popleft()

    if parents[i] != 0:
        parents[j] = i
    elif parents[j] != 0:
        parents[i] = j
    else:
        temp.append((i, j))

# 출력
for idx in range(2, cnt_node + 1):
    print(parents[idx])
'''
def dfs(idx):
    for i in visited[idx]:
        if not parents[i]:
            parents[i] = idx
            dfs(i)


# 노드의 개수
cnt_node = int(input())
# 자식인덱스에 부모 노드 저장할 리스트
parents = [0] * (cnt_node + 1)
# 간선의 수 = 노드의 개수 - 1 만큼 저장
visited = [[] for _ in range(cnt_node + 1)]
for _ in range(cnt_node - 1):
    i, j = map(int, input().split())
    visited[i].append(j)
    visited[j].append(i)

dfs(1)

for idx in range(2, cnt_node + 1):
    print(parents[idx])