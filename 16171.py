#16171: 나는 친구가 적다

S = input("")
K = input("")

for s in S:
    if s.isdigit() == True:
        S = S.replace(s, "")

if S.find(K) >=0:
    print(1)
else:
    print(0)