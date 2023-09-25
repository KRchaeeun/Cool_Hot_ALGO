cnt_city = int(input())
people = list(map(int, input().split()))
graph = [0] + [list(map(int, input().split())) for _ in range(cnt_city)]

