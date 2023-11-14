n = int(input())
fo,ba = input().split('*')
for _ in range(n):
    moon = input()
    if fo == moon[:len(fo)] and ba == moon[len(moon)-len(ba):] and len(fo)+len(ba) <= len(moon):
        print('DA')
    else:
        print('NE')
