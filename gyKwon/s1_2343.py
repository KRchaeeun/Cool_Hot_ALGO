n,m = map(int,input().split())
arr = list(map(int,input().split()))

def bin(s,g):
    if s>g:
        return s
    mid = (s+g)//2
    cnt = 0
    blue = 0
    for i in arr:
        if blue + i > mid:
            cnt += 1
            blue = i
        else:
            blue += i
    if blue:
        cnt += 1
    else:
        pass

    if cnt <= m:
        return bin(s, mid - 1)
    else:
        return bin(mid+1, g)

print(bin(max(arr),sum(arr)))



