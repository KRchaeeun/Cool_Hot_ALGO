# 대기하는 학생수가 최대인 경우와 맨뒤에 줄 서 있는 학생의 번호가 가장 작은 경우를 출력
def max_waiting(infos):
    queue = []  # 학생들의 대기열을 저장하는 리스트 (큐로 사용)
    max_student = 0  # 최대 대기 학생 수를 저장하는 변수
    last_student = []  # 최대 대기 학생 수일 때, 대기열의 마지막 학생 번호를 저장하는 리스트

    for info in infos:
        # 학생 번호가 info[1]인 학생이 대기열의 뒤에 줄을 선다
        if info[0] == 1:
            queue.append(info)
        # 대기 중인 학생 한 명이 식당으로 들어가 식사를 시작한다.
        else:
            queue.pop(0)

        current_length = len(queue)
        # 현재 대기열의 길이를 확인하고, 필요한 경우 최대 대기 학생 수를 갱신한다.
        if current_length > max_student:
            last_student = []  # 최대 대기 학생 수가 갱신되면 last_student를 초기화
            max_student = current_length

        if current_length == max_student and queue:
            last_student.append(queue[-1])  # 마지막 학생의 정보를 리스트에 추가

    # last_student 리스트에서 첫 번째 인덱스 (학생 번호)가 가장 작은 튜플을 찾는다.
    result = min(last_student, key=lambda x: x[1])
    return max_student, result[1]


n = int(input())  # n: 주어질 정보의 개수
infos = []  # infos: 주어진 정보를 튜플 형태로 저장할 빈 리스트
for _ in range(n):
    info = tuple(map(int, input().split()))  # info: 주어진 정보를 튜플로 저장
    infos.append(info)

# print(infos)
print(*max_waiting(infos))  # 출력