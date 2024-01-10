import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def binary_search(start, end):
    if start > end:
        return start

    mid = (start + end) // 2

    sum_v = 0
    idx = 0
    for i in record:
        if sum_v + i > mid:
            idx += 1
            sum_v = 0
        sum_v += i

    if sum_v:
        idx += 1

    if idx > M:
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid - 1)


N, M = map(int, input().split())
record = list(map(int, input().split()))

print(binary_search(max(record), sum(record)))
