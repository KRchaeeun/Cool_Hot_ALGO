import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def find(num1, num2, C, d):
    global print_num
    global S
    global P
    global flag

    if num1 == S:
        if d == P:
            for i in check_dict:
                if check_dict[i] < sen_dic[i] :
                    break
            else:
                if flag != 1:
                    print_num += 1
        return
    
    if sen[C] in check_dict:
        check_dict[sen[C]] += 1
        check_list[C] = 1
        find(num1 + 1, num2, C+1, d + 1)
        check_dict[sen[C]] -= 1
        check_list[C] = 0
    else:
        flag = 1
        check_list[C] = 1
        find(num1 + 1, num2, C+1, d + 1)
        flag = 0
        check_list[C] = 0
    
    find(num1+1, num2, C+1, d)

S, P = map(int, input().strip().split())
flag = 0
print_num = 0
sen = input().strip()
sen_dic = {}
check_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
sen_dic['A'], sen_dic['C'], sen_dic['G'], sen_dic['T'] = map(int, input().strip().split())
check_list = [0] * S
find(0, P, 0, 0)
print(print_num)