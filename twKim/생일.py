import sys
input = sys.stdin.readline

n = int(input())
st = []
for _ in range(n):
    n, d, m, y = input().split()
    st.append([n, int(d), int(m), int(y)])
st.sort(key=lambda x: (x[3], x[2], x[1]))
print(st[-1][0])
print(st[0][0])