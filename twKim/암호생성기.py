for tc in range (1, 11) :
    T = int(input())                            # 처음 테스트케이스 번호를 받아옴

    N_list = list(map(int, input().split()))    # N_list를 받아옴
    while N_list[-1] > 0 :                      # N_list의 끝이 0 이하이면 종료하는 while 문
        for i in range (1,6) :                  # 5번이 한 싸이클로 굴려줌
            N_list.append(N_list.pop(0)-i)      # 싸이클에 맞는 수식을 넣어줌
            
            if N_list[-1] <= 0 :                # 한번 할때마다 N_list의 뒤를 검사해
                break                           # 0 이하이면 for문 탈출
    
    N_list[-1] = 0                              # 음수일 경우를 위해 N_list 뒤를 0으로 만듬
    print(f'#{T}', *N_list)                     # 출력