import sys, collections
input = sys.stdin.readline

def bfs():
    visited = [-1] * (N+1)
    queue = collections.deque()
    queue.append(1)
    visited[1] = 0

    while queue:
        s = queue.popleft()

        for node in tree[s]:
            if visited[node] == -1:
                queue.append(node)
                visited[node] = s

    return visited[2:]


N = int(input())
tree = [[] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    i, j = map(int, input().rstrip().split())
    tree[i].append(j)
    tree[j].append(i)

print(*bfs(), sep='\n')