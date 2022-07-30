#1010

import math

T = int(input());

for i in range(T):
    site1, site2 = input().split();
    site1 = int(site1);
    site2 = int(site2);
    bridge = math.factorial(site2)//(math.factorial(site1)*math.factorial(site2-site1));
    print(bridge);