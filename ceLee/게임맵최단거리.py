def solution(maps):
    from collections import deque
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x, y = queue.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if maps[nx][ny] > 1 or maps[nx][ny] == 0:
                continue
            
            if nx == 0 and ny == 0:
                continue
                
            queue.append((nx, ny))
            maps[nx][ny] += maps[x][y]
    
    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    else:
        return -1