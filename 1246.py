#1246: 온라인 판매

"""
문제:
경래는 닭을 기르는데 올 겨울 달걀 풍년으로 함박 웃음을 짓고 있다. 그리고 이 달걀을 영양란으로 둔갑하여 옥션에 판매하려한다.
경래는 총 N개의 달걀이 있고, 그의 잠재적인 고객은 총 M명이다. 그리고 각각의 i번째 고객은 각자 달걀 하나를 Pi 가격 이하로 살 수 있다고 밝혔다.
경래는 영양란이라 속인 죄책감에 한 고객에게 두 개 이상의 달걀은 팔지 않기로 하였다. 하지만 위의 규칙 하에 수익은 최대로 올리고 싶기에 얼마로 팔지 고민하고 있다.
즉, A가격에 달걀을 판다고 하면 Pi가 A가격보다 크거나 같은 모든 고객은 달걀을 산다는 뜻이다. (물론 달걀 총 수량을 초과하여 팔 수 는 없다)
문제는 이러한 경래를 도와 최대 수익을 올릴 수 있는 달걀의 가장 낮은 가격을 책정하는 것이다.
"""

N, M = map(int, input().split())
pay = []
maxpay = 0
eggpay = 0

for _ in range(M):
    pay.append(int(input()))

pay.sort(reverse=True)

for i in range(M):
    if maxpay <= pay[i] * (i + 1):
        maxpay = pay[i] * (i + 1)
        eggpay = pay[i]
    if i == N - 1:
        break

print(eggpay, maxpay)