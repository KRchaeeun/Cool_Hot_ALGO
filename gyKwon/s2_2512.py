import sys
input = sys.stdin.readline
def bsearch(s,g):
    global suma
    if s>g:
        return g
    mid = (s+g)//2
    avg = 0
    for p in price:
        if p >= mid:
            avg+=mid
        else:
            avg+=p
    if avg > suma:
        return bsearch(s,mid-1)
    else:
        return bsearch(mid+1,g)

n = int(input())
price = list(map(int,input().split()))
suma = int(input())
price.sort()

print(bsearch(1,max(price)))


