import sys
input = sys.stdin.readline
ck = dict()
s = input().rstrip()
s = s.upper()
cnt = 0
for i in s:
    if ck.get(i):
        ck[i] += 1
    else:
        ck[i] = 1
max_val = max(ck.values())
for k, v in ck.items():
    if v == max_val:
        cnt += 1
        res = k
if cnt > 1:
    print("?")
else:
    print(res)
