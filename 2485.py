#2485: 가로수

"""
문제:

"""
import sys
import math

N = int(sys.stdin.readline())
streettree = []
gap = []
cnt = 0

for i in range(N):
    streettree.append(int(input()))
    if i > 0 and i < N:
        gap.append(streettree[i] - streettree[i - 1])

gcd = gap[0]
for i in range(1, len(gap)):
    gcd = math.gcd(gcd, gap[i])

for i in gap:
    cnt += (i // gcd - 1)

print(cnt)

