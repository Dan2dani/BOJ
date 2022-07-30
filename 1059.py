#1059

L = int(input(""));
S = list(map(int, input("").split()));
n = int(input(""));
S.sort();

left = 0;
right = S[0];

for i in range(len(S)):
    if S[i] == n:
        print(0);
        exit();
    if S[i] < n:
        left = S[i];
        right = S[i+1];

print((right - left-2) + ((right-1 - n)*(n-(left+1))));