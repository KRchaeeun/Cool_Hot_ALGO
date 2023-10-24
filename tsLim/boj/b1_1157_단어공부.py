word = input().lower()
word_list = list(set(word))
cnt = []
for i in word_list:
    word_count = word.count(i)
    cnt.append(word_count)
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_list[(cnt.index(max(cnt)))].upper())