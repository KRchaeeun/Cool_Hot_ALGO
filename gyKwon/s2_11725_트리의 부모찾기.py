import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def tree(s):
    # visited[s] = 1 --> 이후 다음 노드의 부모 노드가 1 일 수도 있으니
    # 다른 문제처럼 시작점 방문표시 x
    # dfs 를 활용하여 탐색
    for w in arr[s]:
        if visited[w] == 0:
            # 부모 노드 -> 이 전에 탐색한 노드라고 볼 수 있기 때문에
            # 직전 노드를 visited w 에 방문표시
            visited[w] = s
            tree(w)


N = int(input())
# 1 번 노드부터 활용할 것이기 때문에 N+1
arr = [[] for _ in range(N+1)]
# 연결리스트로 매개변수 받기
for _ in range(N-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(N+1)
tree(1)
# 2번 노드부터 끝까지 출력
for i in range(2,len(visited)):
    print(visited[i])
