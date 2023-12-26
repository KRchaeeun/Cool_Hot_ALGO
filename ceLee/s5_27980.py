import sys
sys.stdin = open("input.txt")


def find_substrings(W, K):
    # 각 문자에 대해 인덱스를 저장하는 딕셔너리
    char_indices = {}
    for i, char in enumerate(W):
        if char in char_indices:
            char_indices[char].append(i)
        else:
            char_indices[char] = [i]

    min_len = float('inf')
    max_len = 0

    for indices in char_indices.values():
        if len(indices) >= K:
            # 가장 짧은 문자열 찾기
            for i in range(len(indices) - K + 1):
                current_len = indices[i + K - 1] - indices[i] + 1
                min_len = min(min_len, current_len)

                # 가장 긴 문자열 찾기
                if i == 0 or W[indices[i - 1]] != W[indices[i]]:
                    j = i + K - 1
                    while j < len(indices) and W[indices[j]] == W[indices[i]]:
                        j += 1
                    max_len = max(max_len, indices[j - 1] - indices[i] + 1)

    if min_len == float('inf'):
        return -1, -1

    return min_len, max_len


T = int(input().strip())

for _ in range(T):
    W = input().strip()
    K = int(input().strip())
    result = find_substrings(W, K)
    print(f"{result[0]} {result[1]}")
