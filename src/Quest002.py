# created: 22:42 2024/10/10 by ZXPrism
# https://tieba.baidu.com/p/9213589527

input_file = open("input.txt")
output_file = open("output.txt", "w")
input = input_file.readline
print = output_file.write

inf = 1 << 30


def solve():
    n = int(input())
    v = list(map(int, input().split()))

    pre = [0] * (n + 1)
    suf = [0] * (n + 1)
    premx = [-inf] * (n + 1)
    sufmx = [-inf] * (n + 1)

    for i in range(n):
        pre[i + 1] = max(pre[i] + v[i], v[i])
        premx[i + 1] = max(premx[i], pre[i + 1])

    for i in range(n - 1, -1, -1):
        suf[i] = max(suf[i + 1] + v[i], v[i])
        sufmx[i] = max(sufmx[i + 1], suf[i])

    ans = -(1 << 31)
    for i in range(n - 1):
        ans = max(ans, premx[i + 1] + sufmx[i + 1])

    print(str(ans) + "\n")


if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        solve()

    input_file.close()
    output_file.close()
