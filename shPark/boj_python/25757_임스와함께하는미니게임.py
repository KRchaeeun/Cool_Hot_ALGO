import sys

# input = sys.stdin.readline

inp = list(input().split())

persons = set()
for i in range(int(inp[0])):
    s = input().rstrip()
    persons.add(s)

res = 0
if inp[1] == 'Y':
    res = len(persons)
elif inp[1] == 'F':
    res = len(persons) // 2
elif inp[1] == 'O':
    res = len(persons) // 3

print(res)
