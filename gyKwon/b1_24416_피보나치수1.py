def fib(n):
    # 교안에 있는거 그대로 파이썬 코드식으로 변환함
    if (n == 1 or n == 2):
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))


def fibonacci(n):
    f= [0]*(n+1) # 먼저 길의 n+1의 배열 생성
    #조건에 따라 인덱스 1,2 는 1의 값을 가짐
    f[1] = 1
    f[2] = 1
    cnt = 0
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]
        cnt += 1
    return cnt
# 정수의 인풋값을 받고
N = int(input())
# 두 함수의 계산 횟수 출력
print(f'{fib(N)} {fibonacci(N)}')