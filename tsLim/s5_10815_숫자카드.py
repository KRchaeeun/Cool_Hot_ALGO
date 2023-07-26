import sys

N = int(sys.stdin.readline())
num_list1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num_list2 = list(map(int, sys.stdin.readline().split()))

result = {}
for i in num_list2:
    result[i] = 0

for j in num_list1:
    if j in result:
        result[j] = 1

for k in result:
    print(result[k], end=' ')