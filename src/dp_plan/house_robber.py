from random import randint
from rich import print

v = [randint(-100, 100) for _ in range(10)]
n = len(v)

print(f"Generated Array: {v}")

dp = [0] * (n + 2)
pred = [(-1, False)] * n  # (a, b): a 表示前驱的下标，b 表示是否选择当前元素

for i in range(n):
    if dp[i + 1] >= dp[i] + v[i]:
        dp[i + 2] = dp[i + 1]
        pred[i] = (i - 1, False)
    else:
        dp[i + 2] = dp[i] + v[i]
        pred[i] = (i - 2, True)

print(f"Maximum Value: {dp[n + 1]}")

plan = []
i = n - 1
while i >= 0:
    if pred[i][1]:
        plan.append(i)
    i = pred[i][0]
plan.reverse()

for i in plan:
    print(f"Select index {i} with value {v[i]}")
