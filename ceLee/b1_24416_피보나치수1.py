# 코드1
def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)

# 코드2
def fib2(n):
    dp = [0] * (n + 1) # n+1길이의 초기값 0으로 설정된 dp리스트
    dp[1], dp[2] = 1, 1 # dp[1], dp[2] 값 1로 설정
    cnt2 = 0 # 카운트를 세기위한 cnt2를 초기값 0으로 설정
    for i in range(3, n + 1):
        cnt2 += 1 # 호출할 때마다 카운트 1씩 증가
        dp[i] = dp[i - 1] + dp[i - 2]
    return cnt2

# 출력
n = int(input())
print(fib1(n), fib2(n))
