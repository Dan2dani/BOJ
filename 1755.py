#1755: 숫자놀이

"""
문제:
79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 80은 마찬가지로 "eight zero"라고 읽는다.
79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.
문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.
"""

digit = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
eng = []
engs = []

N, M = map(int, input().split())

for i in range(N, M + 1):
    if i // 10 == 0:
        eng.append((digit[i], i))
    else:
        eng.append((digit[i // 10] + digit[i % 10], i))

eng = sorted(eng)

for i in range(len(eng)):
    if i % 10 == 0 and i != 0:
        print()
    print(eng[i][1], end=" ")