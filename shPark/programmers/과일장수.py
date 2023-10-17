def solution(k, m, score):
    # 뒤에서 부터 사용
    score.sort()
    answer = 0
    # m개씩 꺼내서 쓸거니까 m 단위로 끊음
    while len(score) >= m:
        # 임시저장소
        tmp = []
        # m 개만 꺼내서
        for _ in range(m):
            tmp.append(score.pop())
        # 최소값에다가 사과의 개수 곱하기
        answer += min(tmp) * m
    return answer
