#1094: 막대기

length = [64]
X = int(input(""))


while sum(length) > X:
    half = length[-1] // 2
    length[-1] = half
    length.append(half)
    if sum(length) - length[-1] >= X:
        length.remove(half)

print(len(length))