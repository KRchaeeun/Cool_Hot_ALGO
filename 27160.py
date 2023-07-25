##지현##

N = int(input())
fruits = ['STRAWBERRY', 'BANANA', 'LIME', 'PLUM']
st = []
ba = []
li = []
pl = []

for _ in range(N):
    S, X = input().split()
    X = int(X)
    
    if S == fruits[0]:
        st.append(X)
    elif S == fruits[1]:
        ba.append(X)
    elif S == fruits[2]:
        li.append(X)
    else:
        pl.append(X)

if sum(st) == 5 or sum(ba) == 5 or sum(li) == 5 or sum(pl) == 5:
    print('YES')
else: print('NO')

##################################################################
##채은##

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

###################################################################
##수형##

# 27160 할리갈리
import sys
input = sys.stdin.readline
n = int(input())
di = dict()
for i in range(n):
    k, v = input().split()
    v = int(v)
    di.setdefault(k,0)
    di[k] += v

if 5 in di.values():
    print('YES')
else:
    print('NO')
 
 ################################################################
 ##태수##

import sys

N = int(sys.stdin.readline())
cards = {
    'STRAWBERRY' : 0,
    'BANANA' : 0,
    'LIME' : 0,
    'PLUM' : 0
}

for i in range(N):
    fruit, x = sys.stdin.readline().split()
    cards[fruit] += int(x)


if 5 in cards.values():
    print('YES')
else:
    print('NO')
##################################################################
##현철##

n = int(input())

fruits = {}
for __ in range(n):
    fruit, num = input().split()
    num = int(num)
    fruits.setdefault(fruit, 0)
    fruits[fruit] = fruits[fruit] + num

if 5 in list(fruits.values()):
    print('YES')
else:
    print('NO')

##################################################################
##근열##

N = int(input())

win_hg = {
    'STRAWBERRY':0,
    'BANANA':0, 
    'LIME':0, 
    'PLUM':0
    }

for i in range(N):
    S,X = input().split()
    win_hg[S] += int(X)
        
if 5 in win_hg.values():
    print("YES")
else:
    print("NO")
