def dfs(cnt, result, add, sub, mul, div):
    global max_v
    global min_v

    # 모든 연산자를 사용한 경우, 결과 값을 갱신
    if cnt == n:
        max_v = max(max_v, result)
        min_v = min(min_v, result)
        return

    # 남은 각 연산자의 개수에 따라서 분기
    if add > 0:
        dfs(cnt + 1, result + num_list[cnt], add-1, sub, mul, div)
    if sub > 0:
        dfs(cnt + 1, result - num_list[cnt], add, sub-1, mul, div)
    if mul > 0:
        dfs(cnt + 1, result * num_list[cnt], add, sub, mul-1, div)
    if div > 0:
        # 나눗셈의 경우, 음수를 양수로 나눌 때의 처리
        dfs(cnt + 1, -((-result) // (num_list[cnt])) if result < 0 else result // num_list[cnt], add, sub, mul, div-1)

# 입력 받기
n = int(input())  # 수의 개수
num_list = list(map(int, input().split()))  # 수열
add, sub, mul, div = map(int, input().split())  # 각 연산자의 개수

# 최댓값과 최솟값 초기화
max_v = -1000000001
min_v = 1000000001

# DFS 시작. 첫 번째 수는 이미 결정되었으므로 cnt는 1로 시작
dfs(1, num_list[0], add, sub, mul, div)

# 결과 출력
print(max_v)
print(min_v)
