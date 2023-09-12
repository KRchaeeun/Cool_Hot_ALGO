T = int(input())

for _ in range(T):
    # 소괄호를 담을 리스트
    brackets = []
    # 정답인지 아닌지 표시하기 위한 변수 ans
    ans = 0

    # 주어진 문자열을 공백 없이 받고,
    txt = input().strip()

    # 문자열의 길이만큼 문자열의 철자 하나를 요소로 가져와
    for i in txt:
        # 만약 문자열이 왼쪽 소괄호일 경우,
        if i == '(':
            # 소괄호를 담는 리스트에 추가해줌
            brackets.append(i)
        # 만약 문자열이 오른쪽 소괄호일 경우,
        elif i == ')':
            # 왼쪽 소괄호가 리스트에 있다면,
            if brackets:
                # 왼쪽 소괄호를 빼냄
                brackets.pop()
            # 왼쪽 소괄호가 리스트에 없다면 오른쪽 소괄호 먼저 나온 것이므로,
            else:
                # 괄호의 짝이 맞지 않으므로 리스트에 넣어주고 더 살펴보는 것을 중단
                brackets.append(i)
                break

    # 만약 각각 리스트에 요소가 없을 경우,
    if not brackets:
        # 모든 괄호들이 짝지어 없어진 것이므로 정답이란 의미로 ans에 1 할당
        ans = 1

    if ans:
        print('YES')
    else:
        print('NO')