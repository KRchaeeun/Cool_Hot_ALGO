N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
Q = [] # 연산을 위한 큐 설정
maxa = 0 # 가장 많이 줄을 서있을 때 몇명이 줄에 서있었는지를 나타내주는 변수
mina = 0 # maxa 당시 맨 뒤에 있던 학생의 번호의 최솟값
for i in range(N):

    if arr[i][0] == 1:
        Q.append(arr[i][1]) # 0번 인덱스가 1인 경우 1번인덱스를 큐에 추가

    else:
        Q.pop(0) # 0번 인덱스가 2인 경우 팝

    if len(Q) > maxa: # 길이의 최댓값 구하기
        maxa = len(Q)
        mina = Q[-1]
    elif len(Q) == maxa: # 길이의 최댓값 구할 당시 맨 뒤 학생 번호 최솟값 구하기
        if mina > Q[-1]:
            mina = Q[-1]

print(maxa,mina)