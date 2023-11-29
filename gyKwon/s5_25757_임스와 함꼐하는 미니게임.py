games = {'Y': 2, 'F': 3, 'O': 4}

N,G = input().split()
fina = set()
for _ in range(int(N)):
    y = input()
    fina.add(y)

if G == 'Y':
    print(len(fina))

elif G == 'F':
    f = len(fina)//2
    print(f)
else:
    o = len(fina)//3
    print(o)