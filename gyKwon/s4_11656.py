from collections import deque

s = list(input())

l = len(s)
a = set()
for i in range(l):
    sl = deque(s)
    for k in range(i):
        sl.popleft()
    sl2 = "".join(sl)
    a.add(sl2)

for j in sorted(a):
    print(j)