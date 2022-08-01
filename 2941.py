#2941: 크로아티아 알파벳

C_A = input("");
count = len(C_A)

for i in range(count):
    if C_A[i] == "=":
        if C_A[i-1] == "c" or C_A[i-1] == "s":
            count -= 1
        if C_A[i-1] == "z":
            count -= 1
            if C_A[i-2] == "d":
                count -= 1
    if C_A[i] == "-":
        if  C_A[i-1] == "c" or C_A[i-1] == "d":
            count -= 1
    if C_A[i] == "j":
        if C_A[i-1] == "l" or C_A[i-1] == "n":
            count -= 1

print(count)