from collections import deque

# 트럭 개수, 다리 길이, 최대 하중
number_of_truck, bridge_dist, max_weight = map(int, input().split())
truck_lst = deque(list(map(int, input().split())))

q = deque()
weight = 0
answer = 0
while truck_lst:
    answer += 1
    truck = truck_lst[0]

    if q and answer - q[0][1] == bridge_dist:
        weight -= q.popleft()[0]

    if weight + truck <= max_weight and len(q) + 1 <= bridge_dist:
        truck = truck_lst.popleft()
        q.append((truck, answer))
        weight += truck

if q:
    answer += bridge_dist

print(answer)

