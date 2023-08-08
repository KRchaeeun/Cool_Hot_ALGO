T = int(input())
for _ in range(T):
    word = input()

    # 스택을 위한 리스트 생성
    rst = []
    for i in word:
        rst += i
        # 만약 0번 인덱스는 '('를 갖은 상태로 )를 갖게 된다면
        # 맨 끝 두개를 삭제한다.
        if rst[0] == '(' and ')' in rst:
            rst.pop()
            rst.pop()

    # 원소의 갯수가 0이면 모두 조건을 충족하여 삭제 된 것이기에 yes
    # 1개 이상이면 NO이다.
    if len(rst) == 0:
        print('YES')
    else:
        print('NO')
