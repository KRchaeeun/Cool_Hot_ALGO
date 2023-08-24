import sys
input = sys.stdin.readline


def candy(arr, N):
    max_row = 0
    max_col = 0
    row_cnt = 1
    col_cnt = 1
    # 열에서 같은거 찾기
    for i in range(N):
        # 다음값을 비교할때 범위를 초과하지 않기 위해서 N-1까지만 반복
        for j in range(N-1):
            # 같으면 카운트
            if arr[i][j] == arr[i][j+1]:
                row_cnt += 1
            # 아니면 1로 바꿈
            else:
                row_cnt = 1
            if max_row < row_cnt:
                max_row = row_cnt
        row_cnt = 1
    # 행에서 같은거 찾기
    for j in range(N):
        # 다음값을 비교할때 범위를 초과하지 않기 위해서 N-1까지만 반복
        for i in range(N-1):
            # 같으면 카운트
            if arr[i][j] == arr[i+1][j]:
                col_cnt += 1
            # 아니면 1로 바꿈
            else:
                col_cnt = 1
            if max_col < col_cnt:
                max_col = col_cnt
        col_cnt = 1
    return max(max_col, max_row)


# 풍선팡의 악몽
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N = int(input())
arr = [list(input()) for _ in range(N)]
res = 0
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 범위 밖에 있을 경우를 모두 제외
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            # 찾을 값과 다를 경우에만 실행
            if arr[i][j] != arr[ni][nj]:
                # 자리 바꿔주기
                arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                # 함수 실행
                count = candy(arr, N)
                if res < count:
                    res = count
                # 다시 원래 위치로 바꿔주기
                arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]

print(res)