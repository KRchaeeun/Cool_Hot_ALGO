import sys

input = sys.stdin.readline

n = int(input())

candies = [list(input().rstrip()) for _ in range(n)]


# 사탕의 연속한 수를 세는 함수
def func(x, y, u, v):
    # 아래 for 문을 1부터 시작할 거라서
    cnt1, cnt2 = 1, 1
    # 카운트를 모아줄 리스트
    f_cnt = []
    # 사탕의 위치를 바꾼다
    candies[x][y], candies[u][v] = candies[u][v], candies[x][y]
    for add_idx in range(1, n):
        # 연속된 사탕의 개수를 세어준다
        if candies[add_idx - 1][y] == candies[add_idx][y]:
            cnt1 += 1
        else:
            f_cnt.append(cnt1)
            cnt1 = 1
        if candies[x][add_idx - 1] == candies[x][add_idx]:
            cnt2 += 1
        else:
            f_cnt.append(cnt2)
            cnt2 = 1
    # 마지막으로 세어준 횟수를 append
    f_cnt.append(cnt1)
    f_cnt.append(cnt2)

    # 원상복구 해줌
    candies[x][y], candies[u][v] = candies[u][v], candies[x][y]

    # 최대값 리턴
    return max(f_cnt)


# 세어준 것들을 저장 해줄 리스트
counts = []
for i in range(n):
    for j in range(n):
        # 델타탐색
        for mi, mj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            di, dj = mi + i, mj + j
            # 유효할 경우만
            if 0 <= di < n and 0 <= dj < n:
                # 찾는다
                counts.append(func(i, j, di, dj))

# 출력
print(max(counts))

# 실패작
"""
sav_counts = []

for i in range(n):
    candy_table_h = {'C': 0, 'P': 0, 'Z': 0, 'Y': 0}
    candy_table_v = {'C': 0, 'P': 0, 'Z': 0, 'Y': 0}
    for j in range(n):
        candy_table_h[candies[i][j]] += 1
        candy_table_v[candies[j][i]] += 1
    max_val = max(candy_table_h.values())
    for k, v in candy_table_h.items():
        if v == max_val:
            sav_counts.append([k, v])
    max_val = max(candy_table_v.values())
    for k, v in candy_table_v.items():
        if v == max_val:
            sav_counts.append([k, v])

max_val = max(sav_counts, key=lambda x: x[1])
idx = sav_counts.index(max_val)
print(max_val, idx)
"""
