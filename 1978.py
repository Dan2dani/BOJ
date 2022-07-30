#1978
N = int(input(""))
count = 0
nums = list(map(int, input().split()))

for i in range(N):
    c = 0;
    for j in range(1, nums[i]+1):
        if nums[i]%j == 0:
            c+=1
    if c == 2:
        count +=1;

print(count)