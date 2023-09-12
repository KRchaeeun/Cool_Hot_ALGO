import sys
input = sys.stdin.readline

def fib(n):
    cnt_fib = 0
    if n == 1 or n == 2:
        cnt_fib += 1
        return cnt_fib
    else:
        return (fib(n-1) + fib(n-2))


def fibonacci(n):
    cnt_fibonacci = 0
    f = [0, 1, 1]
    f += [0] * (n-2)
    f[1] == f[2] == 1 
    for i in range(3, n+1):
        cnt_fibonacci += 1
        f[i] = f[i-1] + f[i-2]
    return cnt_fibonacci


n = int(input())

print(fib(n), fibonacci(n))