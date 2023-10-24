import sys
input = sys.stdin.readline

n = int(input())
q = []
last_min = 0
length = 0

for _ in range(n):
    # 리스트 형태로 입력 받음
    info = list(map(int, input().split()))
    # 앞에 들어오는 값이 1이라면 뒤에 있는 값을 q에 더함
    if info[0] == 1:
        q.append(info[1])
    # 앞에 들어오는 값이 2라면 q에서 pop(0)
    else:
        q.pop(0)

    # 매 반복마다 확인
    if len(q) > length: # 큐의 길이가 저장되어있던 길이보다 길 경우
        length = len(q) # 길이에 큐의 길이 저장
        last_min = q[-1] # 가장 작은 값을 q[-1]에 있는 값으로 저장
    elif len(q) == length: # 큐의 길이와 저장되어 있던 길이와 같을 경우
        if q[-1] < last_min: # 큐의 마지막 값이 저장된 가장 작은값보다 작을경우
            last_min = q[-1] # 가장 작은 값을 큐의 마지막 값으로 바꿔줌

print(length, last_min)