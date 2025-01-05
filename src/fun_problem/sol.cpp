#include <algorithm>
#include <iostream>
#include <ranges>
#include <vector>

using u64 = unsigned long long;
using i64 = long long;

void solve() {
  int x = 0, n = 0, m = 0, k = 0;
  std::cin >> x >> n >> m >> k;

  std::vector<i64> a(n), b(m);
  for (int i = 0; i < n; i++) {
    std::cin >> a[i];
  }
  for (int i = 0; i < m; i++) {
    std::cin >> b[i];
  }

  std::ranges::sort(a, std::greater<>());
  std::ranges::sort(b, std::greater<>());

  std::vector<i64> pre(n + 1);
  for (int i = 0; i < n; i++) {
    pre[i + 1] = pre[i] + a[i];
  }

  constexpr i64 mod = 998'244'353;
  i64 ans = 0;

  int left = std::max(0, k - m), right = std::min(n, k);
  int len = right;
  if (left == 0 && b[k - 1] > 1) {
    if (x * (1 - b[k - 1]) + a[0] >= 0) {
      len = 1;
    } else {
      len = 0;
    }
  } else {
    for (int i = left; i < right; i++) {
      i64 delta = (x + pre[i]) * (1 - b[k - i - 1]) + a[i];
      if (delta <= 0) {
        len = i;
        break;
      }
    }
  }

  i64 add = x, mul = 1;
  for (int i = 0; i < len; i++) {
    add = (add + a[i]) % mod;
  }
  for (int i = 0; i < k - len; i++) {
    mul = mul * b[i] % mod;
  }
  ans = add * mul % mod;

  std::cout << ans << '\n';
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int t = 1;
  while (t--) {
    solve();
  }

  return 0;
}
