# n,m = int(input()), 1

# while True :
#     if 1<<m >= 2 * n :  # 노가다해서 알아낸 규칙이라 설명안됨 왜인지 모름
#         break
#     m += 1

# print(2*n-2**(m-1))     # 마찬가지

import sys
input = sys.stdin.readline

n = int(input())
n_list = [x for x in range (1,n+1)]

while len(n_list) != 1 :

    n_list.pop(0)
    n_list.append(n_list.pop(0))

print(n_list[0])