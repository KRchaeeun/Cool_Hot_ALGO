import sys
input = sys.stdin.readline

sen = input().strip()
len_sen = len(sen)
list_sen = []

for i in range(0, len_sen):
    list_sen.append(sen[i:len_sen])

list_sen = sorted(list_sen)

for i in list_sen :
    print(i)