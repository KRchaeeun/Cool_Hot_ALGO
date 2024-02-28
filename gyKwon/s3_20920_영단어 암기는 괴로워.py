import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dic = {}

for i in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    else:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

finarr = sorted(dic.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in finarr:
    print(i[0])

