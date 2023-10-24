def solution(s):
    answer = ''
    res = ''
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            res += s[i]
            if res in num:
                answer += str(num.index(res))
                res = ''
    return int(answer)