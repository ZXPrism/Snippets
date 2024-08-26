# created: 16:58 2024/8/17 by ZXPrism
# version 02 - optimized
# given main string S and pattern string P
# find the first occurrence of P in S
# Salute to Knuth & Morris & Pratt! (again)

S = "aaaacaaaab"
P = "aaaab"

# 1. precalculate "next" array
# expected next = [-1, -1, -1, -1, 0], if P = "aaaab"
next = [0] * len(P)
next[0] = -1
i = 1
prev = -1
while i < len(P):
    if prev == -1 or P[i - 1] == P[prev]:
        next[i] = next[prev + 1] if P[i] == P[prev + 1] else prev + 1
        prev += 1
        i += 1
    else:
        prev = next[prev]

print("next array: {}".format(next))

# 2. search P in S with the aid of "next" array
i = 0
j = 0
res = -1
while i < len(S):
    if j == -1 or S[i] == P[j]:
        i += 1
        j += 1
        if j == len(P):
            res = i - j
            break
    else:
        j = next[j]

print("ans = {}".format(res))  # expected answer = 5
