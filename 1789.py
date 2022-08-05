#1789: 수들의 합
#서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

import math
N = int(input(""))
i = int(math.sqrt(N))

while True:
    i += 1
    if i * (i + 1) // 2 > N and N - (i * (i + 1) // 2) < i:
        break
print(i - 1)