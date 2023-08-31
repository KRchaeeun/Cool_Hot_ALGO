import sys
sys.stdin = open('input.txt')
# 너비우선탐색
def bfs(si,sj,w,h):
    q = []
    q.append((si,sj))
    # 방문시 arr 에 표시
    arr[si][sj] = '?'
    while q:
        i,j = q.pop(0)
        # 8 방향으로 탐색
        for di,dj in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]:
            ni,nj = i+di,j+dj
            if 0<=ni<h and 0<=nj<w:
                # 해당 좌표값이 1 이라면 큐에 푸쉬 & 어레이에 방문 표시
                if arr[ni][nj] == 1:
                    q.append((ni,nj))
                    arr[ni][nj] = '?'

# 시작좌표값 찾아주는 함수 설정
def wheres(w,h):
    global cnt
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                # 좌표를 찾으면 함수 실행 & 횟수 카운트 +1
                cnt += 1
                bfs(i,j,w,h)

# 인풋 값이 존재할때 까지 반복
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    wheres(w,h)
    print(cnt)