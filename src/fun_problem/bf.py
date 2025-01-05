x, n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

preA = [0] * (n + 1)
for i in range(n):
    preA[i + 1] = preA[i] + a[i]

preB = [1] * (m + 1)
for i in range(m):
    preB[i + 1] = preB[i] * b[i]

ans = 0
mod = 998244353
for i in range(k + 1):
    if i <= n and 0 <= k - i <= m:
        ans = max(ans, (x + preA[i]) * preB[k - i])

print(ans % mod)
