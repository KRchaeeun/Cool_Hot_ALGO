import sys
input = sys.stdin.readline

sentence = list(input().upper().rstrip())
sentence_dict = {}

for i in sentence :

    if i in sentence_dict :
        sentence_dict[i] += 1
    else :
        sentence_dict[i] = 1

sentence_max = max(sentence_dict.values())

if list(sentence_dict.values()).count(sentence_max) == 1 :
    for j in sentence_dict :
        if sentence_dict[j] == sentence_max :
            print(j)

else :
    print('?')