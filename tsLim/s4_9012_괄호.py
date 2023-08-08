T = int(input())
for tc in range(T):
    PS = input()
    stack = []
    for i in PS:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                stack.append(i)
                break
            else:
                stack.pop()
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')