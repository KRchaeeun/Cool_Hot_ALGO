# import sys
from itertools import permutations

def permu(ff):
    global maxa
    global mina
    global finlis
    # permutation 함수를 사용하여 연산자 조합의 경우의 수를 구한다음
    # 앞에서 부터 순차적으로 인덱스를 옮기면서 연산
    # 하나 하나의 경우의 수에서 나온 연산값을 리스트에 넣기
    for pm in permutations(ff,N-1):
        suma = 0
        suma += arr[0]
        for k in range(len(pm)):
            if pm[k] == '+':
                suma += arr[k+1]
            elif pm[k] == '-':
                suma -= arr[k+1]
            elif pm[k] == '*':
                suma *= arr[k+1]
            # 문제 조건에 따라 나누기를 할때 추가적인 연산처리
            else:
                if suma > 0:
                    suma //= arr[k+1]
                else:
                    suma = -(abs(suma)//arr[k+1])
        finlis.append(suma)

N = int(input())
arr = list(map(int,input().split()))
kh = list(map(int,input().split()))
hk = ['+','-','*','//']
ff = []
finlis = []
maxa = -10e9
mina = 10e9
for i in range(len(kh)):
    for j in range(kh[i]):
        ff.append(hk[i])

permu(ff)
print(max(finlis))
print(min(finlis))