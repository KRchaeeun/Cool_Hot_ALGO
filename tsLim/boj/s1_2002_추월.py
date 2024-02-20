import sys

input = sys.stdin.readline

n = int(input())
in_car = {}
out_car = []

# 들어오는건 딕셔너리로 들어온 순서 번호 저장
for i in range(n):
    car = input()
    in_car[car] = i

# 나가는건 그냥 저장
for _ in range(n):
    car = input()
    out_car.append(car)

cnt = 0

# 나가는 순서의 번호가 더 빠를경우에 카운트 증가
for i in range(n-1):
    for j in range(i+1, n):
        if in_car[out_car[i]] > in_car[out_car[j]]:
            cnt += 1
            break

print(cnt)