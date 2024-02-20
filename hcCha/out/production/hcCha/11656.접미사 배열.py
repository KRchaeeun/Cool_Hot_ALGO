word = input()

answer = [word[i:] for i in range(len(word))]

answer.sort()
for i in answer:
    print(i)