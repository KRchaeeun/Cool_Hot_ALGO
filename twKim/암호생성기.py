for tc in range (1, 11) :
    T = int(input())

    N_list = list(map(int, input().split()))
    while N_list[-1] > 0 :
        for i in range (1,6) :
            N_list.append(N_list.pop(0)-i)
            if N_list[-1] < 0 :
                break
    
    N_list[-1] = 0
    print(f'#{tc}', *N_list)