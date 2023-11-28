import sys
input = sys.stdin.readline
import copy

def divide(lst1, lst2):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += (lst1[i][k] * lst2[k][j]) % 1000
    return result



def Divideandconquer(num):

    if num == 1:
        return matrix_the
    
    matrix_d = Divideandconquer(num//2)
    matrix_c = divide(matrix_d, matrix_d)

    if num % 2:
        return divide(matrix_c, matrix_the)
    else:
        return matrix_c


N, B = map(int, input().split())

matrix_the = [list(map(int, input().split())) for _ in range(N)]
matrix_copy = copy.deepcopy(matrix_the)

for i in Divideandconquer(B):
    for j in i:
        print(j % 1000, end=' ')
    print('')