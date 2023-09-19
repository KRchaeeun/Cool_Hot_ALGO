import sys
sys.stdin = open('input.txt')


# 이분탐색
def find_height(start, end):
    # 중심점 지정
    mid = (start + end) // 2
    
    # 딱 안맞아도 가장 근사치 출력
    if start > end:
        return mid
    
    # 자른 나무 길이 측정
    branches = sum([i-mid for i in trees if i-mid > 0])
    
    # 딱맞으면 리턴
    if branches == key:
        return mid
    elif branches > key:
        return find_height(mid + 1, end)
    else:
        return find_height(start, mid - 1)


num_tree, key = map(int, input().split())
trees = list(map(int, input().split()))
print(find_height(0, max(trees)))
