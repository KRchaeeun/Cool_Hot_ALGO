from collections import deque
import sys

# input = sys.stdin.readline

n = int(input())
q = deque()
max_info = [0, 0]
for i in range(n):
    lis = input().rstrip()

    # 앞에가 1이라면 뒤에 숫자를 append
    if lis[0] == '1':
        # lis = list(map(int, lis.split()))
        num = lis[2:]
        q.append(int(num))

    # 2 라면 앞 숫자 하나 pop
    elif lis[0] == '2':
        q.popleft()  # pop(0)

    # 현재 q 의 길이가 저장해 놓은 리스트의 길이보다 길때
    # 바꿔준다
    if len(q) > max_info[0]:
        max_info[0] = len(q)
        max_info[1] = q[-1]

    # 같으면 조건에 따라
    # 마지막 학생의 숫자가 더 작은 경우에만 바꿔준다
    elif len(q) == max_info[0]:
        if q[-1] < max_info[1]:
            max_info[0] = len(q)
            max_info[1] = q[-1]

print(max_info[0], max_info[1])
