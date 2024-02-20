##풀었지만 채은이 답이랑 유사해서 그 대신 시간 초과됐던것 올림!!
import sys
input = sys.stdin.readline

n = int(input())
n_num = list(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))

num = list(set(m_num) - set(n_num))


result = []
for i in m_num:
    if i not in num:
        result.append(1)
    else:
        result.append(0)

print(*result)
