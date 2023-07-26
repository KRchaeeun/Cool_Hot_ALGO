#카드 개수
num_card = int(input())

num_straberry = 0
num_banana = 0
num_lime = 0
num_plum = 0

for i in range(num_card):

    #입력되는 카드 개수
    A, B = input().split()
    #A는 문자열이므로 그대로 나두고 B는 정수열이므로 int로 바꾼다.
    B = int(B)

    #각각의 이름에 따라서 수를 더해준다.
    if A == "STRAWBERRY":
        num_straberry += B
    elif A == "BANANA":
        num_banana += B
    elif A == "LIME":
        num_lime += B
    elif A == "PLUM":
        num_plum += B
    
#마지막으로 나온 결과값들 중에 5가 있으면 'YES', 없으면 'NO'
if num_straberry == 5 or num_banana == 5 or num_lime == 5 or num_plum == 5:
    print('YES')
else:
    print('NO')