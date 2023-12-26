import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
blueray = list(map(int, input().split()))
left, right = max(blueray), sum(blueray)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    record = 0
    for i in range(n):
        if record + blueray[i] > mid:
            cnt += 1
            record = 0
        record += blueray[i]

    if record:
        cnt += 1

    if cnt <= m:
        right = mid - 1
    else:
        left = mid + 1

print(left)