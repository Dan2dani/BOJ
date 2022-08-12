#5635: 생일

#문제:어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.

N = int(input(""))
mem = []
max = 0
min = 0

for _ in range(N):
    person = name, day, month, year = input("").split(" ")
    mem.append(person)

for i in range(1, N):
    if int(mem[i][3]) < int(mem[max][3]):
        max = i
    elif int(mem[i][3]) == int(mem[max][3]):
        if int(mem[i][2]) < int(mem[max][2]):
            max = i
        elif int(mem[i][2]) == int(mem[max][2]):
            if int(mem[i][1]) < int(mem[max][1]):
                max = i

for i in range(1, N):
    if int(mem[i][3]) > int(mem[min][3]):
        min = i
    elif int(mem[i][3]) == int(mem[min][3]):
        if int(mem[i][2]) > int(mem[min][2]):
            min = i
        elif int(mem[i][2]) == int(mem[min][2]):
            if int(mem[i][1]) > int(mem[min][1]):
                min = i


print(mem[min][0])
print(mem[max][0])

