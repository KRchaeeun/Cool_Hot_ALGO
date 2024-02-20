import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

#### 재귀함수 풀이 - 시간초과 메모리 초과
# def check(idx, start, point):
#     global max_v
#
#     if board[start] == meWord[idx]:
#         point += 1
#
#     if idx == M - 1:
#         if max_v < point:
#             max_v = point
#
#     else:
#         for i in [1, -1]:
#             if 0 <= start + i < N:
#                 check(idx + 1, start + i, point)
#
#
# N, M = map(int, input().rstrip().split())
# board = list(input().rstrip())
# meWord = list(input().rstrip())
#
# max_v = 0
# for i in range(N):
#     check(0, i, 0)
#
# print(max_v)