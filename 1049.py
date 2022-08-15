#1049: 기타줄
#패키지(6개씩)

N, M =map(int, input("").split(" "))
pack =[]
unit = []
total_price = []

for _ in range(M):
    pack_price, unit_price = map(int, input("").split(" "))
    pack.append(pack_price)
    unit.append(unit_price)

price = min(pack) * (N // 6) + min(unit) * (N % 6)
total_price.append(price)
price = min(unit) * N
total_price.append(price)
price = min(pack) * (N // 6 + 1)
total_price.append(price)

print(min(total_price))

