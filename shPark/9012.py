import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    # 본 리스트
    lis = list(input().rstrip())
    # 체크해 줄 리스트
    ck = []
    # 리스트의 개수 만큼
    for _ in range(len(lis)):
        # 맨 뒤에것을 받는다
        s = lis.pop()
        # 만약 체크해줄 리스트에 무언가 있다면
        if len(ck):
            # 조건에 맞게 탐색
            if s == '(' and ck[len(ck)-1] == ')':
                ck.pop()
            # 아니라면 뒤에 넣는다
            else:
                ck.append(s)
        # 아무것도 들어있지 않다면 그냥 넣어준다
        else:
            ck.append(s)
    # 끝난뒤 만약 ck 리스트에 무언가 들어있다면 NO 출력
    # 아무것도 없이 비어있으면 YES
    if len(ck):
        print('NO')
    else:
        print('YES')
