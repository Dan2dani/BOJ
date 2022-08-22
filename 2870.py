#2870: 수학숙제

"""
문제:
상근이는 수학시간에 딴 짓을 하다가 선생님께 걸렸다. 선생님은 상근이에게 이번 주말동안 반성하라며 엄청난 숙제를 내주었다.
선생님이 상근이에게 준 종이에는 숫자와 알파벳 소문자로 되어있는 글자가 N줄있다. 상근이는 여기서 숫자를 모두 찾은 뒤, 이 숫자를 비내림차순으로 정리해야한다. 숫자의 앞에 0이 있는 경우에는 정리하면서 생략할 수 있다.
글자를 살펴보다가 숫자가 나오는 경우에는, 가능한 가장 큰 숫자를 찾아야 한다. 즉, 모든 숫자의 앞과 뒤에 문자가 있거나, 줄의 시작 또는 끝이어야 한다.
예를 들어, 01a2b3456cde478에서 숫자를 찾으면 1, 2, 3456, 478이다.
선생님이 준 종이의 내용이 주어졌을 때, 상근이의 숙제를 대신하는 프로그램을 작성하시오.
"""

N = int(input())
note = []
nums = []

for _ in range(N):
    note.append(input())

for k in range(N):
    left = 0
    i = 0
    while i < len(note[k]):
        right = len(note[k])
        if note[k][i].isdigit() == True:
            left = i
            for j in range(i, len(note[k])):
                if note[k][j].isdigit() == False:
                    right = j
                    break
            i = j
            nums.append(int(note[k][left: right]))
        i += 1

for num in sorted(nums):
    print(num)