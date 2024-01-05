n = int(input())

incar = {}
for k in range(n):
    car = input()
    incar[car] = k

cnt = 0
outcar = []
for _ in range(n):
    car = input()
    outcar.append(car)

for i in range(n-1):
    for j in range(i+1,n):
        if incar[outcar[i]] > incar[outcar[j]]:
            cnt += 1
            break

print(cnt)
