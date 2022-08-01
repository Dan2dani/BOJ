#7568: 덩치

N = int(input(""))
body = []
ranklist =[]

for i in range(N):
    b =[]
    weight, height = input("").split()
    b.append(int(weight))
    b.append(int(height))
    body.append(b)

for i in range(N):
    rank = 1
    for j in range(N):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            rank += 1
    ranklist.append(rank)
    print(ranklist[i], end=" ")

    
_____________________________________________________________________________

#7568: 덩치

N = int(input(""))
members = []

for i in range(N):
    body = weight, height = list(map(int, input("").split()))
    members.append(body)

for i in members:
    rank = 1
    for j in members:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ") 
