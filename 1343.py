#1343: 폴리오미노

"""
문제: 민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB
이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.
폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.
"""

board = input("")
poly =""
left = 0
right = len(board)

for i in range(len(board)):
    if board[i] == ".":
        right = i
        if (right - left) % 2 != 0:
            print(-1)
            exit(0)
        for j in range((right - left)//4):
            poly += "AAAA"
        for j in range((((right - left) % 4)) // 2):
            poly += "BB"
        left = i + 1
        poly = poly + "."
    i += 1
    right = len(board)

if (right - left) % 2 != 0:
    print(-1)
    exit(1)
for j in range((right - left) // 4):
    poly += "AAAA"
for j in range((((right - left) % 4)) // 2):
    poly += "BB"

print(poly)