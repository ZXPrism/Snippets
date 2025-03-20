# created: 17:52 2025/02/14 by ZXPrism
# https://tieba.baidu.com/p/9493215341

from rich import print

# dp[i][j] 表示使用 i 位数字构成数位之和为 j 的方案的总数（可包含前导零）
dp = [[0] * 37 for _ in range(5)]

dp[0][0] = 1
for i in range(1, 5):
    for j in range(37):
        for k in range(min(10, j + 1)):
            dp[i][j] += dp[i - 1][j - k]

ans = 0

for i in range(1, 5):
    for j in range(37):
        for k in range(1, min(10, j + 1)):
            ans += dp[i - 1][j - k] * dp[i][j]

print(ans)
