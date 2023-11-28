import sys

# input = sys.stdin.readline

info = []
for _ in range(int(input())):
    s = list(input().split())
    date = s[3]
    if len(s[2]) < 2:
        date += '0'
    date += s[2]
    if len(s[1]) < 2:
        date += '0'
    date += s[1]
    info.append([s[0], int(date)])
info.sort(key=lambda x: x[1])
print(info[-1][0])
print(info[0][0])
