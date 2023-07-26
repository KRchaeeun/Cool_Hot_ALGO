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