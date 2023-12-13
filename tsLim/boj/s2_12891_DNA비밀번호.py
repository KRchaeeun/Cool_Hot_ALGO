S, P = map(int, input().split())
dna = input().rstrip()
a, c, g, t = map(int, input().split())
acgt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# 초기값 계산
pwd = dna[:P]
for j in pwd:
    acgt[j] += 1

cnt = 0
if acgt['A'] >= a and acgt['C'] >= c and acgt['G'] >= g and acgt['T'] >= t:
    cnt += 1

# 문자열의 위치를 옮기면서 앞에 한글자를 빼고 맨 뒷글자를 추가하는 방식으로 계산
for i in range(len(dna)-P):
    acgt[dna[i]] -= 1
    acgt[dna[i+P]] += 1
    if acgt['A'] >= a and acgt['C'] >= c and acgt['G'] >= g and acgt['T'] >= t:
        cnt += 1

print(cnt)