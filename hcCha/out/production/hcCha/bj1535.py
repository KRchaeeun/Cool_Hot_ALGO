import sys
input = sys.stdin.readline

# 사람 수, 잃는 체력, 얻는 기쁨
cnt_human = int(input().strip())
lose = list(map(int, input().strip().split()))
get = list(map(int, input().strip().split()))

# 출력값
max_v = 0
# 수열 인덱스 생성
for i in range(1 << cnt_human):
    hp = 100
    happy = 0
    for j in range(cnt_human):
        if i & (1 << j):
            # 체력과 기쁨 계산
            hp -= lose[j]
            happy += get[j]
    # 체력이 1이상인 경우 최대 행복 계산
    if hp > 0:
        max_v = max(max_v, happy)
print(max_v)