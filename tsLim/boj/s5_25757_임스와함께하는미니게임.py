import sys
input = sys.stdin.readline

N, play = input().split()
N = int(N)
arr = set()
for _ in range(N):
    arr.add(input())

if play == 'Y':
    print(len(arr)//1)
elif play == 'F':
    print(len(arr)//2)
else:
    print(len(arr)//3)