N = int(input(""));
S = dict();
SS = dict();

for i in range(N):
    value = input("");
    S[value] = len(value);

S = sorted(S.items());

for i in range(len(S)):
    SS[S[i][0]] = S[i][1];

SS = sorted(SS.items(), key=lambda x:x[1]);

for i in range(len(SS)):
    print(SS[i][0]);