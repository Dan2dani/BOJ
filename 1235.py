#1235: 학생 번호

"""
문제:
학생들의 번호가 주어 졌을 때, 뒤에서 k자리만을 추려서 남겨 놓았을 때 모든 학생들의 학생 번호를 서로 다르게 만들 수 있는 최소의 k를 구하는 프로그램을 작성하시오.
"""

import sys

N = int(sys.stdin.readline())
student_nums = []

for _ in range(N):
    student_nums.append(sys.stdin.readline().strip())

for i in range(len(student_nums[0]) - 1, -1, -1):
    flag = 0
    for j in range(N - 1):
        for k in range(j + 1, N):
            if student_nums[j][i: len(student_nums[0])] == student_nums[k][i: len(student_nums[0])]:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        print(len(student_nums[0]) - i)
        break