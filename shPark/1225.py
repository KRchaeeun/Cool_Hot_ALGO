T = 10
for tc in range(1, T+1):
    n = int(input())
    password_can = list(map(int, input().split()))
    cnt = 1
    while True:
        # 맨 앞에걸 1, 2, 3, 4, 5 순으로 뺀다.
        password_can[0] -= cnt

        # 1보다 작아진다면 값을 0으로 고정하고
        # 맨 뒤로 보낸뒤 break
        if password_can[0] < 1:
            password_can[0] = 0
            password_can.append(password_can.pop(0))
            break

        # 맨 앞에걸 빼서 뒤로 보낸다
        password_can.append(password_can.pop(0))

        # count 를 세던것이 5를 초과하면
        # 조건에 따라 1로 바꿔준다.
        cnt += 1
        if cnt > 5:
            cnt = 1

    print(f'#{tc}', *password_can)