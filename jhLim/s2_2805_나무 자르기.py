import sys
input = sys.stdin.readline

def binary(l, r):
    ans = 0
    m = (l + r) // 2

    if l > r:
        return m
    
    for i in range(N):
        if tree[i]-m >= 0:
            ans += tree[i]-m

            if i != (N-1) and ans > M:
                return binary(m + 1, r)

    if ans == M:
        return m
    elif ans > M:
        return binary(m + 1, r)
    else:
        return binary(l, m - 1)


N, M = map(int, input().rstrip().split())
tree = list(map(int, input().rstrip().split()))
tree.sort()

print(binary(0, max(tree)))