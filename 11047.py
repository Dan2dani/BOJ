#11047: 동전0

"""
문제:
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
"""

N, K = map(int, input("").split(" "))
val = []
cnt = 0
for _ in range(N):
    val.append(int(input("")))

for i in range(len(val) - 1, -1, -1):
    if K // val[i] > 0:
       cnt += K // val[i]
       K -= (val[i] * (K // val[i]))
    if K == 0:
        break

print(cnt)