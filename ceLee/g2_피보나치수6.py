import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10**9)
'''
Fn+1 = Fn + Fn-1, Fn = Fn
[(Fn+1),(Fn)] = ([(1, 1), (1, 0)]) * [(Fn), (Fn-1)]
                ([(1, 1), (1, 0)]**n) * [(F1), (F0)]
'''

def binary_multiply(matrix, n):
    if n == 1:
        return matrix
    else:
        if n % 2 == 0:
            return binary_multiply(multiply_matrix(matrix, matrix), n//2)
        else:
            return multiply_matrix(binary_multiply(matrix, n-1), matrix)


def multiply_matrix(matrix1, matrix2):  # 행렬 곱하는 함수
    multi_result = [[0]*len(matrix2[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(2):
                sum += matrix1[i][k] * matrix2[k][j]
            multi_result[i][j] = sum % 1000000007  # 나누고 저장해도 뒤에는 더하는데 문제 없음.
    return multi_result


n = int(input())
basic_matrix = [[1, 1], [1, 0]]
start = [[1], [0]]
if n < 3:
    print(1)
else:
    print(multiply_matrix(binary_multiply(basic_matrix, n-1), start)[0][0])