lst = []
for _ in range(5):
    a = int(input())
    lst.append(a)

lst.sort()

print(int(sum(lst)/5))
print(lst[2])