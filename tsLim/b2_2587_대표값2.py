import sys
n_list = []
cnt = 0

for i in range(5):
    n = int(sys.stdin.readline())
    n_list.append(n)
    cnt += n

n_list.sort()

print(cnt // 5)
print(n_list[2])

