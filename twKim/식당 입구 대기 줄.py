import sys
input = sys.stdin.readline

N = int(input())

max_people = 0
people = 0
people_number = 0

for i in range (N) :
    N_list = list(map(int, input().split()))    # for 문 돌때마다 N_list를 새로 받아줄 예정

    if N_list[0] == 1 :                         # 받은 0번 인덱스가 1 이면
        people += 1                             # 사람 수 한개 늘려줌

        if max_people < people :                # 늘린 시점에서 사람 수가 max 보다 많으면 갱신
            max_people = people
            people_number = N_list[1]

        elif max_people == people :             # max_people이 겹치면 
            if people_number > N_list[1] :      # 그 시점에 사람 번호를 비교해서
                people_number = N_list[1]       # 더 작은 번호로 갱신
                
    else : 
        people -= 1                 # 나머지는 사람 빼줌

print(max_people, people_number)