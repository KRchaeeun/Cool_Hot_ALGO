T = int(input())

for tc in range(1,T+1):
    X = input()
    stack = []

    what = True
    for i in X:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')