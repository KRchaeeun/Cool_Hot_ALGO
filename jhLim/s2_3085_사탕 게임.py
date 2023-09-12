import sys
input = sys.stdin.readline

# 행 탐색
def fx(arr, N):
    max_cnt = 0
    for x in range(N):
        cnt = 1
        for y in range(N-1):
            if arr[x][y] == arr[x][y+1]:
                cnt += 1
            else:
                cnt = 1

            if max_cnt < cnt:
                max_cnt = cnt
    
    return max_cnt


# 열 탐색
def fy(arr, N):
    max_cnt = 0
    for y in range(N):
        cnt = 1
        for x in range(N-1):
            if arr[x][y] == arr[x+1][y]:
                cnt += 1
            else:
                cnt = 1

            if max_cnt < cnt:
                max_cnt = cnt
    
    return max_cnt


N = int(input().rstrip())
c = [list(input().rstrip()) for _ in range(N)]
ans_set = set()

# 오른쪽 바꾸기
for x in range(N):
    for y in range(N-1):
        if c[x][y] != c[x][y+1]:
            c[x][y], c[x][y+1] = c[x][y+1], c[x][y]

            # 탐색 시작
            cntx = fx(c, N)
            cnty = fy(c, N)

            ans_set.add(max(cntx, cnty))

            # 다시 원래대로
            c[x][y+1], c[x][y] = c[x][y], c[x][y+1]

# 아래 바꾸기
for y in range(N):
    for x in range(N-1):
        if c[x][y] != c[x+1][y]:
            c[x][y], c[x+1][y] = c[x+1][y], c[x][y]

            # 탐색 시작
            cntx = fx(c, N)
            cnty = fy(c, N)

            ans_set.add(max(cntx, cnty))

            # 다시 원래대로
            c[x+1][y], c[x][y] = c[x][y], c[x+1][y]

print(max(ans_set))