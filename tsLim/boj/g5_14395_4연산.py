from collections import deque

s, t = map(int, input().split())

if s==t:
    print(0)
elif t==1:
    print('/')
else:
    visited = set()
    q = deque()
    q.append((s, ''))
    while q:
        n, n_str = q.popleft()
        if n == t:
            print(n_str)
            break
        else:
            if n * n <= 10**9 and n * n not in visited:
                q.append((n*n, n_str+'*'))
                visited.add(n*n)
            if n + n <= 10** 9 and n + n not in visited:
                q.append((n+n, n_str+'+'))
                visited.add(n+n)
            if n / n not in visited:
                q.append((n/n, n_str+'/'))
                visited.add(1)
    else:
        print(-1)