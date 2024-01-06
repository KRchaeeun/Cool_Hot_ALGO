import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())

truck = list(map(int, input().split()))

# 다리 크기만큼 0으로 해서 생성
bridge = [0] * w

time = 0

while bridge:
    # 시간이 1초 지나가면 다리 제일 앞은 pop
    time += 1
    bridge.pop(0)
    # 아직 트럭들이 남아있을 때
    if truck:
        # 다리 위의 트럭 무게와 들어올 트럭 무게가 L을 넘지 않으면 추가
        if sum(bridge) + truck[0] <= L:
            bridge.append(truck.pop(0))
        # 아니면 0을 추가하여 진행
        else:
            bridge.append(0)

print(time)