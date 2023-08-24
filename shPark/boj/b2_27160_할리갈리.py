import sys
input = sys.stdin.readline
n = int(input())
di = dict()
for i in range(n):
    k, v = input().split()
    v = int(v)
    di.setdefault(k,0)
    di[k] += v

if 5 in di.values():
    print('YES')
else:
    print('NO')