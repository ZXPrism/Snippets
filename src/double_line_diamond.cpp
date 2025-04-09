// created: 14:42 2025/4/2 by ZXPrism
// https://tieba.baidu.com/p/9618741144

#include "bits/stdc++.h"

using u64 = unsigned long long;
using i64 = long long;

void solve()
{
    char c = 0;
    int n = 0;
    scanf("%d %c", &n, &c);
    for (int i = 0; i < 2 * n; i++)
    {
        for (int j = 0; j < 2 * n - 1; j++)
        {
            int det = abs(n - 1 - i + (i >= n)) + abs(n - 1 - j);
            putchar((det >= n - 2 && det < n ? c : ' '));
        }
        putchar('\n');
    }
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t = 1;
    // std::cin >> t;
    while (t--)
    {
        solve();
    }

    return 0;
}
