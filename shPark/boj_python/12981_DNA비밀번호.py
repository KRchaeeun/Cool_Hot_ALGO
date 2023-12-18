# import sys

# input = sys.stdin.readline

# s, p = map(int, input().split())
# dna = list(input().rstrip())
# limits = list(map(int, input().split()))

# res = 0
# answer_sheet = {'A': 0, 'C':0, 'G':0, 'T':0}



# for i in range(s-p+2):
#     answer_sheet['A'] = 0
#     answer_sheet['C'] = 0
#     answer_sheet['G'] = 0
#     answer_sheet['T'] = 0

#     for dna_part in dna[i:i+p]:
#         if dna_part == 'A':
#             answer_sheet['A'] += 1
#         elif dna_part == 'C':
#             answer_sheet['C'] += 1
#         elif dna_part == 'G':
#             answer_sheet['G'] += 1
#         elif dna_part == 'T':
#             answer_sheet['T'] += 1
#         if answer_sheet['A'] >= limits[0] and answer_sheet['C'] >= limits[1] and answer_sheet['G'] >= limits[2] and answer_sheet['T'] >= limits[3]:
#             res += 1
#             break

# print(res)

import sys
input = sys.stdin.readline


S, P = map(int, input().split())
dna = input().rstrip()
a, c, g, t = map(int, input().split())
acgt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

pwd = dna[:P]
for j in pwd:
    acgt[j] += 1

cnt = 0
if acgt['A'] >= a and acgt['C'] >= c and acgt['G'] >= g and acgt['T'] >= t:
    cnt += 1

for i in range(len(dna)-P):
    acgt[dna[i]] -= 1
    acgt[dna[i+P]] += 1
    if acgt['A'] >= a and acgt['C'] >= c and acgt['G'] >= g and acgt['T'] >= t:
        cnt += 1

print(cnt)