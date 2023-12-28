import sys
sys.stdin = open("input.txt")  

n, m = map(int, input().split())
money = []
for _ in range(n):
    data = int(input())
    money.append(data)  

left = max(money)
right = sum(money)  
  
while left <= right:
    mid = (left + right) // 2

    total_money = 0
    cnt = 0  
    for i in range(n):
        if total_money + money[i] > mid:
            cnt += 1
            total_money = 0
        total_money += money[i]
    
    if total_money:
        cnt += 1

    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1

print(mid)