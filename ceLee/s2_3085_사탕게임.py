# count_longets: 배열에서 같은 글자의 길이가 가장 큰 길이를 반환하는 함수
def count_longest(arr, N):
    max_val = -1  # max_val: 가장 큰 길이를 저장할 변수, 초기값 -1
    for i in range(N):  # 열 탐색
        cnt = 1
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:  # 다음 문자와 길이가 같으면 길이에 1 추가
                cnt += 1
            else:  # 다르면 저장되어있는 max_val과 cnt중 큰 것을 max_val에 저장
                max_val = max(max_val, cnt)
                cnt = 1  # cnt 초기화
        max_val = max(max_val, cnt)

    for j in range(N):  # 행 탐색
        cnt = 1
        for i in range(N-1):
            if arr[i][j] == arr[i+1][j]:
                cnt += 1
            else:
                max_val = max(max_val, cnt)
                cnt = 1
        max_val = max(max_val, cnt)
    return max_val

# swap_and_count: 두 글자의 위치를 서로 바꾸고 count_longest 함수를 호출해서 제일 긴 문자열을 max_count에
# 저장 후 배열 원래대로 돌려놓기
def swap_and_count(arr, N, i1, j1, i2, j2):
    arr[i1][j1], arr[i2][j2] = arr[i2][j2], arr[i1][j1]
    max_count = count_longest(arr, N)
    arr[i1][j1], arr[i2][j2] = arr[i2][j2], arr[i1][j1]
    return max_count

N = int(input())  # 보드의 크기 N X N
arr = [list(map(str, input())) for _ in range(N)]  # arr: 보드 문자를 입력 받기

result = 0  # result: 최종적으로 제일 긴 문자 길이를 저장할 변수, 초기값 0
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            result = m```ax(result, swap_and_count(arr, N, i, j, i, j+1))  # 가로로 문자 바꾸기
        if i + 1 < N:
            result = max(result, swap_and_count(arr, N, i, j, i+1, j))  # 세로로 문자 바꾸기
print(result)  # 출력