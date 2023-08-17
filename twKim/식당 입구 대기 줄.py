import sys
input = sys.stdin.readline

N = int(input())

max_people = 0
people = 0
people_number = 0
for i in range (N) :
    N_list = list(map(int, input().split()))
    if N_list[0] == 1 :
        people += 1

        if max_people < people :
            max_people = people
            people_number = N_list[1]
    else : 
        people -= 1

print(max_people, people_number)