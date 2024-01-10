N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]

home.sort()

start = (1 + (home[-1] - home[0])) // 2
