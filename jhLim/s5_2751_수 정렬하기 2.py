import sys
input = sys.stdin.readline

li = []
n = int(input())

for i in range(n):
    a = int(input())
    li.append(a)

li.sort()

for i in range(n):
    print(li[i])