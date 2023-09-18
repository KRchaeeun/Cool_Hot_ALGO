def bin(l, h):
    # dap 이라는 변수에 최종 출력값 담기
    global dap
    # 종료 조건
    if l > h:
        return
    # 중간 값 설정
    mid = (l + h) // 2
    # 반복문 돌려서 문제 조건에 따라 절단기 높이 설정 후
    # 나무 높이에서 절단기 높이를 빼준 값들을 다 더해서 fin으로 값 받기
    fin = 0
    for a in trees:
        if a > mid:
            fin += a - mid
    # 가져가야 할 나무 높이만큼 가져왔으면
    # 절단기의 높이(mid)를 dap 이라는 변수에 담기
    if fin == M:
        dap = mid
        return
    # 가져가야 할 나무의 높이보다 덜 가져오면
    # 절단기의 높이를 낮추기 --> 여기서 반대로 생각해서 계속 헤맴
    elif fin < M:
        bin(l, mid - 1)
    # 위의 케이스와 반대로 적용
    elif fin > M:
        dap = mid
        bin(mid + 1, h)

N, M = map(int, input().split())
trees = list(map(int, input().split()))
# 이진 탐색을 할 것이기 때문에 정렬
trees.sort()
dap = 0
bin(0, trees[-1])
print(dap)