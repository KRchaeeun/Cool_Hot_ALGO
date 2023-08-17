
for tc in range(1,11):
    tt = int(input())
    arr = list(map(int, input().split()))
    a = 0 # 조건에 맞게 1씩 증가하는 변수
    
    while True:
        # arr 0번 인덱스를 팝
        v = arr.pop(0)
        a += 1
        # a  = 5 초과시 1로 돌아와야함
        if a > 5:
            a = 1
        # v-a가 0 이하인 경우 0으로 출력되게 하고, 맨뒤가 0이 되면 멈추는 조건 설정
        va = v-a
        if va <= 0:
            va = 0
            arr.append(va)
            break
        # 아닌 경우 v -a하고 큐에 추가
        else:
            v -= a
            arr.append(v)



    print(f'#{tc}',*arr)