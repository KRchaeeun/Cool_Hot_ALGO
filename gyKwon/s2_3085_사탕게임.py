# import sys
# sys.stdin = open('input.txt')
N = int(input())
arr = [list(input()) for _ in range(N)]
maxa = 0
# 행 위주 탐색
for i in range(N):
    for j in range(1,N):
        # 인접한 두 값 바꿔주기
        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
        # 바꾼 상태에서 행 위주 탐색
        for k in range(N):
            cnt = 1
            for p in range(1,N):
                # 인접 값 이 같다면 cnt +1
                if arr[k][p] == arr[k][p-1]:
                    cnt+=1
                    #####실행 할 때 마다 맥스값 초기와(안 하면 행 넘어갈때 카운트 안 됨)###
                    maxa = max(maxa, cnt)
                else:
                    # 같지 않다면 맥스값과 비교 후 카운트 초기화
                    if cnt>maxa:
                        maxa = cnt
                        cnt = 1
                    else:
                        cnt = 1
        # 열 위주 탐색 (내용은 똑같음)
        for p in range(N):
            cnt = 1
            for k in range(1,N):
                if arr[k][p] == arr[k-1][p]:
                    cnt+=1
                    maxa = max(maxa, cnt)
                else:
                    if cnt>maxa:
                        maxa = cnt
                        cnt = 1
                    else:
                        cnt = 1
        # 인접 값 바꾼 후 탐색을 한 다음 종료시 다시 원위치로 돌려주기
        arr[i][j], arr[i][j - 1] = arr[i][j - 1], arr[i][j]
# 열 위주 탐색 (위의 내용과 동일)
for j in range(N):
    for i in range(1,N):
        arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
        for k in range(N):
            cnt = 1
            for p in range(1, N):
                if arr[k][p] == arr[k][p - 1]:
                    cnt += 1
                    maxa = max(maxa, cnt)
                else:
                    if cnt > maxa:
                        maxa = cnt
                        cnt = 1
                    else:
                        cnt = 1

        for p in range(N):
            cnt = 1
            for k in range(1, N):
                if arr[k][p] == arr[k - 1][p]:
                    cnt += 1
                    maxa = max(maxa, cnt)
                else:
                    if cnt > maxa:
                        maxa = cnt
                        cnt = 1
                    else:
                        cnt = 1
        arr[i][j], arr[i - 1][j] = arr[i - 1][j], arr[i][j]

print(maxa)