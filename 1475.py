#1475: 방 번호

N = input("")
digit =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in N:
    digit[int(i)] += 1

if (digit[6] + digit[9]) % 2 == 0:
    digit[6] = (digit[6] + digit[9]) // 2
else:
    digit[6] = (digit[6] + digit[9] ) // 2 + 1

digit[9] = 0

print(max(digit))



