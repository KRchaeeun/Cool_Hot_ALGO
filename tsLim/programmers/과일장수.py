def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score) >= m:
        res = []
        for _ in range(m):
            res.append(score.pop())
        answer += (min(res)*m)
    return answer