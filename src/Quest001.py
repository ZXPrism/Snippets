# created: 12:49 2024/8/27 by ZXPrism
# https://tieba.baidu.com/p/9147134720
# solve a^x = m, find the smallest natural number a or report the number doesn't exist
from math import log

m = int(input())
up = 10

ansA = -1
ansX = -1

for a in range(2, up + 1):
    L = 1
    R = int(log(m) // log(a)) + 1
    while L < R:
        M = (L + R) >> 1
        if pow(a, M) >= m:
            R = M
        else:
            L = M + 1
    if pow(a, L) == m:
        ansA = a
        ansX = L
        break

if ansA == -1:
    for x in range(int(log(m) // log(10)), 0, -1):
        L = 11
        R = m + 1
        while L < R:
            M = (L + R) >> 1
            if pow(M, x) >= m:
                R = M
            else:
                L = M + 1
        if pow(L, x) == m:
            ansA = L
            ansX = x
            break

print((ansA, ansX) if ansA != -1 else 0)
