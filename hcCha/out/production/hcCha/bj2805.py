def binary_search(start, end):
    mid = (start + end) // 2

    if start > end:
        return mid

    sum_tree = 0
    for i in tree:
        if i - mid >= 0:
            sum_tree += i - mid

    if sum_tree == need_tree:
        return mid
    elif sum_tree > need_tree:
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid - 1)


cnt_tree, need_tree = map(int, input().split())
tree = list(map(int, input().split()))

print(binary_search(0, max(tree)))

