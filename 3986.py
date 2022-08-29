#3986: 좋은 단어

"""
문제:


"""
import sys
N = int(sys.stdin.readline())
words = []
cnt = 0

for _ in range(N):
    words.append(sys.stdin.readline().strip())

for i in range(N):
    word = []
    for j in range(len(words[i])):
        if len(word) == 0 or word[-1] != words[i][j]:
            word.append(words[i][j])
        elif word[-1] == words[i][j]:
            word.pop()
    if len(word) == 0:
        cnt += 1

print(cnt)