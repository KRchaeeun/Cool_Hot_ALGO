p, s = map(int, input().split())
dna = input()
a, c, g, t = map(int, input().split())
dit = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
cnt = 0


for i in range(s):
    dit[dna[i]] += 1

def cnta(dit):
    return dit['A'] >= a and dit['C'] >= c and dit['G'] >= g and dit['T'] >= t

if cnta(dit):
    cnt += 1

for i in range(1, p - s + 1):
    dit[dna[i - 1]] -= 1
    dit[dna[i + s - 1]] += 1
    if cnta(dit):
        cnt += 1

print(cnt)