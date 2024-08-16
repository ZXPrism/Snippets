# created: 13:46 2024/8/16 by ZXPrism
# version 01
# given main string S and pattern string P
# find the first occurrence of P in S
# Salute to Knuth & Morris & Pratt!

S = "ababcbababcabxyz"
P = "ababcab"

# 1. precalculate "next" array
# expected next = [-1, 0, 0, 1, 2, 0, 1], if P = "ababcab"
next = [0] * len(P)
next[0] = -1
i = 2
k = 0
while i < len(P):
    if k == -1 or P[i - 1] == P[k]:
        next[i] = k + 1
        i += 1
        k += 1
    else:
        k = next[k]

print("next array: {}".format(next))

# 2. search P in S with the aid of "next" array
res = -1
i = 0
k = 0
while i < len(S):
    if k == -1 or S[i] == P[k]:
        k += 1
        i += 1
        if k == len(P):
            res = i - k
            break
    else:
        k = next[k]


print("ans = {}".format(res))  # expected answer = 6
