rv = list(input().upper())
# 알파벳을 키값으로 하는 딕셔너리 생성
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ditto = {}
for a in alpha:
    ditto[a] = 0
    # 딕셔너리 키값이랑 입력된 글자랑 비교해서 겹치는 키값 +1
alpha_keys = list(ditto.keys())
for r in rv:
    for k in alpha_keys:
        if r == k:
            ditto[k] += 1

eta = list(ditto.items())

eta.sort(key=lambda x:x[1]) # 람다 함수 활용해서 튜블 1번 인덱스의 정수 오름차순으로 정렬

# 튜블 1번 인덱스 값이 겹치는 것이 있다면 물음표를 출력하게 만듦
sb = 0
for zz in range(len(eta)-1):
    if eta[zz][1] == eta[-1][1]:
        sb += 1

if sb == 0:
    print(eta[-1][0])
else :
    print('?')


