cnt1 = 0
cnt2 = 0

# 문제 조건에서 준 재귀호출 의사 코드
def fib(n):
    global cnt1
    if n == 1 or n == 2: # if( n = 1 or n = 2)
        return 1 # return 1
    else:
        cnt1 += 1  # 카운트 세기
        return fib(n-1) + fib(n-2) # 재귀호출

# 문제 조건에서 준 동적 프로그래밍 의사 코드
def fibonacci(n):
    global cnt2
    f[1], f[2], = 1, 1 # f[1] <- f[2] <- 1
    for i in range(3, n+1): # for i <- 3 to n
        cnt2 += 1 # 카운트 세기
        f[i] = f[i-1] + f[i-2] # f[i] <- f[i-1] + f[i-2]
    return f[n]


f = [0 for _ in range(41)] # n의 개수가 5<=n<=40까지이기 때문에 40 크기의 리스트 생성
n = int(input())
fib(n) # 각각의 함수 호출
fibonacci(n) # 각각의 함수 호출
print(cnt1 + 1, cnt2) # 마지막에 호출한 횟수를 카운트를 못했기 때문에 cnt1에는 1 추가