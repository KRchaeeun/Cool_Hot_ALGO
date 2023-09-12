import sys
input = sys.stdin.readline

a = list(input().rstrip())

# 소문자이면 대문자로 전환
for i in range(len(a)):
    if a[i].islower():
        a[i] = a[i].upper()

dit = {}
# 알파벳을 키값으로 딕셔너리
for i in a:
    if dit.get(i) is None:
        dit[i] = 1
    else:
        dit[i] += 1

# 값을 추출하여 max 값을 구하고,
lst = list(dit.values())
max_v = max(lst)

# 만약 max값이 중복일경우 ? 출력
if lst.count(max_v) != 1:
    print('?')

# 만약 max값이 중복이 아닐 경우 해당 알파벳 출력
else:
    con_dit = {v:k for k,v in dit.items()}
    print(con_dit.get(max_v))
