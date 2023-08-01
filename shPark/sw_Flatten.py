import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))


    def my_max(li):
        res = 0
        for i in li:
            if i > res:
                res = i
        return res


    def my_min(li):
        res = 1e6
        for i in li:
            if i < res:
                res = i
        return res


    for _ in range(n):
        max_val, min_val = my_max(li), min(li)
        if max_val - min_val <= 1:
            break
        li[li.index(max_val)] -= 1
        li[li.index(min_val)] += 1
    print(f'#{tc} {max(li) - min(li)}')