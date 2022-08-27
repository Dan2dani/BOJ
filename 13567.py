#13567: 로봇

"""
문제:

"""
import sys
ways = ["right", "down", "left", "up"]

M, n = map(int, sys.stdin.readline().split())
x = 0
y = 0
way = 0
flag = 0

for _ in range(n):
    opt, num = sys.stdin.readline().split()
    way %= 4
    if opt == "MOVE":
        if ways[way] == "right":
            x += int(num)
        elif ways[way] == "down":
            y -= int(num)
        elif ways[way] == "left":
            x -= int(num)
        elif ways[way] == "up":
            y += int(num)
    else:
        if int(num) == 0:
            way -= 1
        else:
            way += 1
    if x > M or y > M or x < 0 or y < 0:
        flag = 1

if flag == 1:
    print(-1)
else:
    print(x, y)