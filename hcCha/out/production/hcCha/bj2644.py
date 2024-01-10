def check():
    global cnt1
    global cnt2
    while child_parents[now]:
        cnt1 += 1
        now = child_parents[now]

    while child_parents[next]:
        cnt2 += 1
        next = child_parents[next]


cnt_peoele = int(input())
now, next = map(int, input().split())
cnt_edge = int(input())
child_parents = [0] * (cnt_peoele + 1)

for _ in range(cnt_edge):
    parents, child = map(int, input().split())
    child_parents[child] = parents

cnt1 = 0
cnt2 = 0

if now == next:
    print(cnt1 + cnt2)
else:
    print(-1)
