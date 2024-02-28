import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    prior = list(map(int, input().split()))
    arr = deque()
    for i in range(N):
        arr.append((prior[i],i+1))

    arr2 = sorted(arr)
    