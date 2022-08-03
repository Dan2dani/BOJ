#1676: 팩토리얼 0의 개수

#문제: N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

import math

N = int(input(""))
fac = str(math.factorial(N))
count = 0

for i in range(len(fac) -1 , -1, -1):
    if int(fac[i]) > 0:
        break
    else:
        count+=1
print(count)
