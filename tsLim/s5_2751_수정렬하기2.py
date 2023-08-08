import sys

N = int(sys.stdin.readline())
n_list = []

for i in range(N):
    k = int(sys.stdin.readline())
    n_list.append(k)

n_list.sort()

for j in range(len(n_list)):
    print(n_list[j])

    