def f(day, benefit):
    global res
    if day == n:
        res = max(res, benefit)
        return
    if day > n:
        return

    f(day+t[day], benefit+p[day])
    f(day+1, benefit)
    pass


n = int(input())
t = [0] * n
p = [0] * n

for i in range(0, n):
    t[i], p[i] = map(int, input().split())
res = 0
f(0, 0)
print(res)