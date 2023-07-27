import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())

H = C // 60
M = C % 60

B += M
A += H

if B >= 60:
    A = A+1
    B = B-60

if A >= 24:
    A = A-24

print(A, B)