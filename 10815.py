##채은##

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

#################################################################

##수형##
#1
## 10815 숫자카드
import sys
input = sys.stdin.readline
n = int(input())
card = dict()
card_list = map(int, input().split())

for i in card_list:
    card[i] = 1

m = int(input())

num_list = map(int, input().split())

for i in num_list:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')

#2

# 10815 숫자카드 이분탐색
import sys
input=sys.stdin.readline

def finf(li,a):
    start=0;end=len(li)-1

    while start<=end:
        mid=(start+end)//2

        if li[mid]==a:
            return 1
        elif li[mid]<a:
            start=mid+1
        else:end=mid-1

    return 0

n=int(input())

li_1=list(map(int,input().split()))

m=int(input())

li_2=list(map(int,input().split()))

li_1.sort()

for i in li_2:
    sys.stdout.write(str(finf(li_1,i))+' ')
#################################################################

##근열##

import sys
N = int(sys.stdin.readline())
N_list = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for i in M_list:

    if i in N_list:

        print('1', end=" ")
    else:
        print('0', end=" ")

###################################################################

##태수##

import sys

N = int(sys.stdin.readline())
num_list1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num_list2 = list(map(int, sys.stdin.readline().split()))

result = {}
for i in num_list2:
    result[i] = 0

for j in num_list1:
    if j in result:
        result[j] = 1

for k in result:
    print(result[k], end=' ')

#################################################################

##지현##

import sys
input = sys.stdin.readline

N = int(input())
n_set = set(input().split())
# print(n_lst)
# print(type(n_lst))

M = int(input())
m_lst = input().split()

rs = []

for i in m_lst:
    if i in n_set:
        rs.append(1)
    else: rs.append(0)

print(*rs)

##############################################################
##현철##
##풀었지만 채은이 답이랑 유사해서 그 대신 시간 초과됐던것 올림!!
import sys
input = sys.stdin.readline

n = int(input())
n_num = list(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))

num = list(set(m_num) - set(n_num))


result = []
for i in m_num:
    if i not in num:
        result.append(1)
    else:
        result.append(0)

print(*result)
