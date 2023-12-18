import sys

# input = sys.stdin.readline

for _ in range(int(input())):
    # 문자열 리스트
    string_list = list(input())
    # 숫자로 치환
    n_string_list = list(map(lambda x: ord(x)-97, string_list))
    arr = [0] * 30
    # 포함할 문자열 개수
    n = int(input())
    start = 0
    end = 0
    res1, res2 = 1e9, 0
    arr[n_string_list[start]] = 1
    arr[n_string_list[end]] = 1

    max_len = len(string_list)
    while start <= end:
        if arr[n_string_list[end]] == n:
            arr[n_string_list[start]] -= 1
            start += 1
            if n_string_list[start] == n_string_list[end]:
                tmp = sum(arr)
                res1 = min(tmp, res1)
                res2 = max(tmp, res2)
        else:
            if end < max_len - 1:
                end += 1
                arr[n_string_list[end]] += 1
            elif start < max_len - 1:
                start += 1
                arr[n_string_list[start]] -= 1
            else:
                break

    if res1 <= res2:
        print(res1, res2)
    else:
        print(-1)
