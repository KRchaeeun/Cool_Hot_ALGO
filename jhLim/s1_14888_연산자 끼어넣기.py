import sys, itertools
input = sys.stdin.readline

N = int(input().rstrip())
numlst = list(map(int, input().rstrip().split()))
oplst = list(map(int, input().rstrip().split()))
lst = []
mini = 1e10
maxi = -1e10

for i in range(4):
    for _ in range(oplst[i]):
        lst.append(i+1)

case = list(itertools.permutations(lst, len(lst)))

for c in case:
    cnt = numlst[0]
    for i in range(1, N):
        if c[i-1] == 1:
            cnt += numlst[i]
        elif c[i-1] == 2:
            cnt -= numlst[i]
        elif c[i-1] == 3:
            cnt *= numlst[i]
        elif c[i-1] == 4:
            if cnt < 0:
                cnt = -((-cnt)//numlst[i])
            else:
                cnt //= numlst[i]
                
    if cnt > maxi:
        maxi = cnt
    if cnt < mini:
        mini = cnt

print(maxi)
print(mini)