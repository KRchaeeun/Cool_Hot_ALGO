import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)
while start <= end:
    can_take = 0
    mid = (start + end)//2
    for tree in trees:
        if tree > mid:
            can_take += tree - mid
    if can_take >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)