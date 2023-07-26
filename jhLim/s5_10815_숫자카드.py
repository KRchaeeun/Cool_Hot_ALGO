import sys
input = sys.stdin.readline

N = int(input())
n_set = set(input().split())
# print(n_lst)
# print(type(n_lst))

M = int(input())
m_lst = input().split()

rs = []

for i in m_lst:
    if i in n_set:
        rs.append(1)
    else: rs.append(0)

print(*rs)