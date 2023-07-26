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