from random import randint
from rich import print

T = 100
N = int(2e5)


def Test_EmptySubseqAllowed(lb: int, ub: int):
    v = [randint(lb, ub) for _ in range(N)]
    ok_cnt = 0

    print("Test: empty subsequences are allowed")
    for _ in range(T):
        # greedy approach
        ans_greedy = 0
        for elem in v:
            if elem > 0:
                ans_greedy += elem

        # DP approach
        dp = [0] * (N + 1)
        for i in range(N):
            dp[i + 1] = max(dp[i], dp[i] + v[i])
        ans_dp = dp[N]

        if ans_greedy == ans_dp:
            ok_cnt += 1

    print(f"{ok_cnt} tests[green] PASSED[/], {T - ok_cnt} tests[red] FAILED[/]\n")


def Test_EmptySubseqNotAllowed(lb: int, ub: int):
    v = [randint(lb, ub) for _ in range(N)]
    ok_cnt = 0

    print("Test: empty subsequences are NOT allowed")
    for _ in range(T):
        # greedy approach
        ans_greedy = 0
        has_nonneg_elem = False
        for elem in v:
            if elem >= 0:
                ans_greedy += elem
                has_nonneg_elem = True
        if not has_nonneg_elem:
            ans_greedy = max(v)

        # DP approach
        dp = [0] * (N + 1)
        dp[0] = -(1 << 18)
        for i in range(N):
            dp[i + 1] = max(dp[i], dp[i] + v[i], v[i])
        ans_dp = dp[N]

        if ans_dp == ans_greedy:
            ok_cnt += 1

    print(f"{ok_cnt} tests[green] PASSED[/], {T - ok_cnt} tests[red] FAILED[/]\n")


Test_EmptySubseqAllowed(-1000000000, 1000000000)
Test_EmptySubseqAllowed(0, 1000000000)
Test_EmptySubseqAllowed(-1000000000, -1)

Test_EmptySubseqNotAllowed(-1000000000, 1000000000)
Test_EmptySubseqNotAllowed(0, 1000000000)
Test_EmptySubseqNotAllowed(-1000000000, -1)
