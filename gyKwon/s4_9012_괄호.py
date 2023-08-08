T = int(input())

for tc in (1,T+1):
    X = input()
    aa = 0
    bb = 0
    for i in X:
        if i == '(':
            aa += 1
        elif i == ')':
            bb += 1

    if aa == bb:
        print('YES')
    else:
        print('NO')

    