import sys

# input = sys.stdin.readline

n = int(input())

fld = [0] * 1001

sticks = []

for _ in range(n):
    l, h = map(int, input().split())
    sticks.append(l)
    fld[l] = h

# sticks.sort(key=lambda x: x[0])
max_val = max(sticks)

sav = 0
for i in range(1001):
    if fld[i] > sav:
        sav = max(fld[i], sav)
    else:
        fld[i] = sav
    if i+1 == max_val:
        break

print(sum(fld))
# print(max_val)
