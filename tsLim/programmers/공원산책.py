def solution(park, routes):
    h = len(park)
    w = len(park[0])
    delta = {
        'S': [1, 0],
        'N': [-1, 0],
        'E': [0, 1],
        'W': [0, -1]
    }
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x = i
                y = j

    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        flg = 0
        dx = x
        dy = y
        for i in range(1, distance + 1):
            dx += delta[direction][0]
            dy += delta[direction][1]
            if dx >= h or dx <= -1 or dy >= w or dy <= -1 or park[dx][dy] == 'X':
                flg = 1
                break

        if flg == 0:
            x += delta[direction][0] * distance
            y += delta[direction][1] * distance
    answer = [x, y]
    return answer