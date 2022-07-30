#1316
N = int(input(""))
count = 0;

for i in range(N):
    word = input("")
    chk = 0
    for j in range(len(word)):
        for k in range(j+1, len(word)):
            if word[j] == word[k] and word[j] != word[j+1]:
                chk+=1
    if chk == 0:
        count+=1

print(count)