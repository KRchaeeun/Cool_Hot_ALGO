
'''
def combination(idx, rst):
    global revenue
    if rst:
        if sum(rst) > max_honey:
            return

    if idx == cnt_box:
        temp = 0
        for i in rst:
            temp += i ** 2
        revenue = max(revenue, temp)
        return

    else:
        combination(idx + 1, rst + [possible[idx]])
        combination(idx + 1, rst + [])


for tc in range(1, int(input()) + 1):

    size, cnt_box, max_honey = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(size)]

    # 가로로만 가능
    delta = [i for i in range(cnt_box)]
    idx = 0
    rst = []
    for i in range(size):
        for j in range(size - cnt_box + 1):
            revenue = 0
            idx += 1
            get_honey = 0
            possible = []
            for k in delta:
                possible.append(matrix[i][j + k])

            combination(0, [])
            # for honey in possible:
            #     if get_honey + honey > max_honey:
            #         break
            #     get_honey += honey
            #     revenue += honey ** 2
            rst.append((revenue, idx))

    rst.sort(reverse=True)
    ans = 0
    avoid = []
    idx = 0
    for v, k in rst:
        if k in avoid:
            continue
        temp = k // (size - cnt_box + 1)

        if k % (size - cnt_box + 1) == 0:
            # for i in range(1, cnt_box):
            #     if temp != (k - i) // (size - cnt_box + 1):
            #         continue
            #     avoid.append(k - i)
            for i in range(k, k - (size - cnt_box + 1), -1):
                avoid.append(i)

        # elif k % (size - cnt_box + 1) == 1:
        #     for i in range(1, cnt_box):
        #         if temp != (k + i) // (size - cnt_box + 1):
        #             continue
        #         avoid.append(k + i)

        else:
            # for i in range(1, cnt_box):
            #     if temp == (k - i) // (size - cnt_box + 1):
            #         avoid.append(k - i)
            #     if temp == (k + i) // (size - cnt_box + 1):
            #         avoid.append(k + i)
            k += k % (size - cnt_box + 1)
            for i in range(k, k - (size - cnt_box + 1), -1):
                avoid.append(i)

        ans += v
        idx += 1
        if idx == 2:
            break
    print(f'#{tc}', ans)
'''  # 망한 코드
# 두 명의 일꾼을 합쳐 최대 수익을 구해야하지만
# 한 명의 최대수익을 구하고 다른 한 명을 구해버림
# 8 9 9 8 의 경우 8, 9 / 9, 8로 구해야 하지만 9, 9로 구해서 양 옆 8, 8은 사용할 수 없게 됨
# 이런 실수는 두 번 다시 하면 안됨;

