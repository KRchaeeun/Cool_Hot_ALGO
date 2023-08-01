# 1
## 10815 숫자카드
import sys

input = sys.stdin.readline
n = int(input())
card = dict()
card_list = map(int, input().split())

for i in card_list:
    card[i] = 1

m = int(input())

num_list = map(int, input().split())

for i in num_list:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')

# 2

# 10815 숫자카드 이분탐색

# import sys
#
# input = sys.stdin.readline
#
#
# def finf(li, a):
#     start, end = 0, len(li) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if li[mid] == a:
#             return 1
#         elif li[mid] < a:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#     return 0
#
#
# n = int(input())
#
# li_1 = list(map(int, input().split()))
#
# m = int(input())
#
# li_2 = list(map(int, input().split()))
#
# li_1.sort()
#
# for i in li_2:
#     sys.stdout.write(str(finf(li_1, i)) + ' ')
