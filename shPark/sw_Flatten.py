import sys
sys.stdin = open('input.txt')


# bubble 정렬 구현
def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


T = 10
for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))

    for _ in range(n):
        li = bubble_sort(li)
        res = li[-1] - li[0]

        # 정렬 후 최대, 최소가 1보다 작거나 같은지 확인
        if res <= 1:
            break
        
        # 조건문을 거치지 않았다면 각각 최대와 최소의 1을 빼고, 더하기
        li[0] += 1
        li[-1] -= 1
    
    # 마지막으로 정리
    li = bubble_sort(li)
    res = li[-1] - li[0]
    
    # 출력
    print(f'#{tc} {res}')


# def my_max(li):
#     res = 0
#     for i in li:
#         if i > res:
#             res = i
#     return res
#
#
# def my_min(li):
#     res = 1e6
#     for i in li:
#         if i < res:
#             res = i
#     return res
#
#
# T = 10
# for tc in range(1, T + 1):
#     # dump 횟수
#     n = int(input())
#     # 손봐줘야 되는거
#     li = list(map(int, input().split()))
#
#     for _ in range(n):
#         max_val, min_val = my_max(li), my_min(li)
#         if max_val - min_val <= 1:
#             break
#         # max 값의 인덱스를 찾고 해당 값에서 1을 뺀다
#         """
#         max_val = max(li)
#         idx = li.index(max_val)
#         li[idx] -= 1
#         max_val 값에대한 li의 index 번호를 return 해줌
#         """
#         li[li.index(max_val)] -= 1
#         # min 값의 인덱스를 찾고 해당 값에서 1을 더한다
#         li[li.index(min_val)] += 1
#
#     print(f'#{tc} {my_max(li) - my_min(li)}')
