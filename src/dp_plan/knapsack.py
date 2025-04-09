from random import randint
from rich import print

n = 10
weight = [randint(1, 100) for _ in range(n)]
value = [randint(1, 100) for _ in range(n)]
MAXW = sum(weight) // randint(1, 5)

print(f"Generated Maximum Allowed Weight: {MAXW}")
print(f"Generated Weights: {weight}")
print(f"Generated Values: {value}")

dp = [[0] * (MAXW + 1) for _ in range(n + 1)]
pred = [[(-1, -1, False)] * (MAXW + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(MAXW + 1):
        dp[i + 1][j] = dp[i][j]
        pred[i + 1][j] = (i, j, False)
        if j >= weight[i] and dp[i][j - weight[i]] + value[i] > dp[i + 1][j]:
            dp[i + 1][j] = dp[i][j - weight[i]] + value[i]
            pred[i + 1][j] = (i, j - weight[i], True)

print(f"Maximum Value: {dp[n][MAXW]}")

plan = []
i, j = n, MAXW
while i >= 1:
    if pred[i][j][2]:
        plan.append(i - 1)
    new = (pred[i][j][0], pred[i][j][1])
    i, j = new
plan.reverse()

for i in plan:
    print(f"Select item #{i} with weight {weight[i]} and value {value[i]}")
