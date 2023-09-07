import sys

input = sys.stdin.readline


def recursion(cnt, num):
    global max_num
    global min_num

    if cnt == N:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return

    for i in range(4):
        if operator_list[i]:
            if i == 0:
                operator_list[i] -= 1
                recursion(cnt + 1, num + N_list[cnt])
                operator_list[i] += 1
            elif i == 1:
                operator_list[i] -= 1
                recursion(cnt + 1, num - N_list[cnt])
                operator_list[i] += 1
            elif i == 2:
                operator_list[i] -= 1
                recursion(cnt + 1, num * N_list[cnt])
                operator_list[i] += 1
            elif i == 3:
                operator_list[i] -= 1
                if num < 0:
                    recursion(cnt + 1, -(-num // N_list[cnt]))
                else :
                    recursion(cnt + 1, num // N_list[cnt])
                operator_list[i] += 1


N = int(input())
N_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))
max_num = -float('inf')
min_num = float('inf')
recursion(1, N_list[0])
print(max_num)
print(min_num)