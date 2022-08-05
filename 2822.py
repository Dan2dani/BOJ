#2822: 점수 계산
"""
상근이는 퀴즈쇼의 PD이다.
이 퀴즈쇼의 참가자는 총 8개 문제를 푼다.
참가자는 각 문제를 풀고, 그 문제를 풀었을 때 얻는 점수는 문제를 풀기 시작한 시간부터 경과한 시간과 난이도로 결정한다. 문제를 풀지 못한 경우에는 0점을 받는다. 참가자의 총 점수는 가장 높은 점수 5개의 합이다.
상근이는 잠시 여자친구와 전화 통화를 하느라 참가자의 점수를 계산하지 않고 있었다. 참가자의 8개 문제 점수가 주어졌을 때, 총 점수를 구하는 프로그램을 작성하시오.
"""
score = {}
num = []
result = 0

for i in range(1, 9):
    score[i] = int(input(""))

for i in range(5):
    max_key = max(score, key = score.get)
    num.append(max_key)
    result += score[max_key]
    del(score[max_key])

print(result)
num.sort()

for i in num:
    print(i, end=" ")