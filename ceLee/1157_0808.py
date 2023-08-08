import sys
sys.stdin = open("input.txt")

# 주어진 알파벳을 대문자로 변환
word = input().upper()

# 알파벳의 빈도를 저장할 리스트 초기화(대문자는 총 26개)
alphabet_count = [0] * 26

# 각 알파벳의 빈도를 계산
for char in word:
    alphabet_count[ord(char) - ord('A')] += 1

# 가장 많이 나온 알파벳의 빈도수
max_count = 0 # 초기값 0
for i in range(26):
    if alphabet_count[i] > max_count:
        max_count = alphabet_count[i]

# 가장 많이 나온 알파벳이 여러개 일 수 있으므로 max_count_index에 index값을 저장
max_count_index = []
for i in range(26):
    if alphabet_count[i] == max_count:
        max_count_index.append(i)

# 가장 많이 나온 알파벳이 하나이면 그 문자를 프린트하고 여러개이면 ?를 출력
if len(max_count_index) == 1:
    # max_count_index가 하나이면 인덱스가 0인 수 하나이므로 그 수에다 유니코드 A의 수를 더한 후 문자로 바꾸기
    print(chr(max_count_index[0] + ord('A')))
else:
    print('?')