import sys
sys.stdin = open("input.txt")

T = int(input())

for _ in range(T):

    # 주어진 괄호 문자열 저장
    bracket_string = input().strip()

    # push하고 pop할 빈 리스트
    stack = []

    # VPS인지 아닌지 판단할 is_VPS, 초기값은 True
    is_VPS = True

    for char in bracket_string:
        if char == "(": # 왼쪽 괄호이면 stack에 push 하기
            stack.append(char)
        else: # 오른쪽 괄호일 때
            # 스택에 있으면 마지막에 있는 문자 stack에서 pop하기
            if stack:
                stack.pop()
            # 스택에 없으면 VPS가 아니므로 is_VPS를 False로 저장 후 그만(break)
            else:
                is_VPS = False
                break

    # 결과 출력
    # 만약 VPS이고 stack에 아무것도 없다면 YES, 둘 중 하나라도 만족 못하면 NO
    if is_VPS and not stack:
        print("YES")
    else:
        print("NO")
