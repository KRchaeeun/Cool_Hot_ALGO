moon1 = input()

len0 = 0
len1 = 0

moon = []
for i in moon1:
    if int(i) == 0:
        len0 += 1
        moon.append(i)
    else:
        len1 += 1
        moon.append(i)

moon.reverse()
cnt0 = 0
for k in moon:
    if int(k) == 0:
        moon.remove(k)
        cnt0 +=1
        if cnt0 == len0//2:
            break

moon.reverse()
cnt1 = 0
for j in moon:
    if int(j) == 1:
        moon.remove(j)
        cnt1 += 1
        if cnt1 == len1//2:
            break

fina = ""
for p in moon:
    fina += p
print(fina)