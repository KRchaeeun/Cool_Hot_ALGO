T = int(input())
for tc in range(1, T + 1):
    # 입렵
    # k 갈 수 있는 거리, n 로드의 길이, m 충전소 개수
    k, n, m = map(int, input().split())
    # 충전소 위치
    chg_sp = list(map(int, input().split()))
    # 길 만들기
    mp = [0] * (n + 1)
    # 현재 위치
    cnt = 0
    # 횟수
    res = 0
    # 길에 충전소 설치
    for i in chg_sp:
        mp[i] += 1
    # 횟수 탐색
    while True:
        # 현재 위치에서부터 K부터 K - M까지 중
        # 가장 먼 위치부터 탐색
        for i in range(k, 0, -1):
            # 만약 충전소가 설치되어 있다면
            if mp[cnt + i]:
                # 현재위치 수정
                cnt += i
                # 횟수 추가
                res += 1
                break
        # 현재위치부터 K만큼 내에 없으면 횟수를 0으로 초기화 하고
        # break
        else:
            res = 0
            break
        # 만약에 종착점을 벗어나면 break
        if cnt + k >= n:
            break
    # 출력
    print(f'#{tc} {res}')
