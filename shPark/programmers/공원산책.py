dirc = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}
fld = []


def solution(park, routes):
    # 거리랑 길이 재기
    n, m = 0, 0
    # 시작점 찾기
    start1 = 0
    for i in park:
        tmp = []
        n += 1
        # 시작점 초기화
        start2 = 0
        for j in i:
            tmp.append(j)
            if j == "S":
                x = start1
                y = start2
            start2 += 1
        fld.append(tmp)
        start1 += 1
    m = len(i)
    for i in routes:
        order_dir, dist = i.split()
        dist = int(dist)
        nx, ny = x, y
        for _ in range(dist):
            nx += dirc[order_dir][0]
            ny += dirc[order_dir][1]
            # 조건에 따라서
            if 0 <= nx < n and 0 <= ny < m:
                if fld[nx][ny] == "X":
                    break
            else:
                break
        # 조건에 완벽히 만족할 경우에만 좌표 갱신
        else:
            x = nx
            y = ny

    answer = [x, y]

    return answer