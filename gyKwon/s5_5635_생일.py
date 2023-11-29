import sys
input = sys.stdin.readline

n = int(input())
names = []
for _ in range(n):
    n,d,m,y = input().split()
    names.append([n,int(d),int(m),int(y)])

names.sort(key=lambda x :(x[-1], x[-2], x[-3]))

print(names[-1][0])
print(names[0][0])