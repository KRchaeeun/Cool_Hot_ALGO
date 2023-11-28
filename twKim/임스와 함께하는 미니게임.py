import sys
input = sys.stdin.readline

N, G = map(str, input().split())
N = int(N)
p_set = set()
for i in range(N):
    P = input().strip()
    p_set.add(P)

p_len = len(p_set)

if G == 'Y':
    print(p_len)
elif G == 'F':
    print(p_len//2)
else :
    print(p_len//3)