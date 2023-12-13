s = input().rstrip()

result = []
# 한글자씩 떼서 리스트에 저장
for i in range(len(s)):
    a = s[i:]
    result.append(a)
# 정렬
result.sort()
# 출력
for j in result:
    print(j)