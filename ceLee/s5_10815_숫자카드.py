#상근이 카드 개수
num_playercard = int(input())


"""시간 초과2...
#상근이 카드 리스트
player_list = list(map(int, input().split()))
"""

#상근이의 숫자 카드는 배열이 중요하지 않기 때문에 list보다 더 빠른 set 사용
player_set = set(map(int, input().split()))

#비교할 카드 개수
num_givencard = int(input())

"""시간 초과2...
#비교할 카드 리스트
given_list = list(map(int, input().split()))
"""

#비교할 카드 리스트는 순서가 중요하므로 list 사용
given_list  = list(map(int, input().split()))

#결과값이 출력될 빈 리스트
result_list = []

"""시간 초과1...
for i in range(len(given_list)):
    result_list.append(0)
"""

"""시간 초과1...
for i in range(len(given_list)):
    for j in range(len(player_list)):
        
        #비교할 카드 i번째가 상근이 카드 리스트에 있으면 1
        if given_list[i] == player_list[j]:
            result_list[i] = 1
            break

        #없으면 0을 입력
        else:
            result_list[i] = 0
"""

for num in given_list:
    if num in player_set:
        result_list.append(1)
    else:
        result_list.append(0)

#출력 방법1
print(*result_list)

# #출력 방법2
# print(', '.join(str(i) for i in lst))