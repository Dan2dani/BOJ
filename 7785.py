#7785: 회사에 있는 사람

"""
상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다.
로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.
"""

mem = dict()
names = []
N = int(input(""))

for i in range(N):
    name, state = input("").split(" ")
    mem[name] = state

for key, value in mem.items():
    if value != 'leave':
        names.append(key)

names = sorted(names, reverse = True)

for name in names:
    print(name)