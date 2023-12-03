import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    name, dd, mm, yyyy = input().split()
    dd = int(dd)
    mm = int(mm)
    yyyy = int(yyyy)
    arr.append((name, dd, mm, yyyy))
arr.sort(key=lambda x : (-x[3], -x[2], -x[1]))
print(arr[0][0])
arr.sort(key= lambda x : (x[3], x[2], x[1]))
print(arr[0][0])