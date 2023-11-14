T = int(input())
for _ in range(T):
    w = input()
    k = int(input())

    cdict = {}
    for c in w:
        if c in cdict:
            cdict[c] +=1
        else:
            cdict[c] = 1


    findict = {}

    for i in range(len(w)):
        if cdict[w[i]] >= k:
            num = 1
            length = 1
            for j in range(i+1,len(w)):
                num +=1
                length +=1
                if w[j] == w[i] and length == k:
                    findict[w[i]] = min(findict[w[i]],length)

    print(findict)