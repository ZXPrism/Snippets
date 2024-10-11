# created: 23:01 2024/10/10 by ZXPrism
# https://tieba.baidu.com/p/9213589527

input_file = open("input.txt")
output_file = open("output_bf.txt", "w")
input = input_file.readline
print = output_file.write

inf = 1 << 30


def solve():
    n = int(input())
    v = list(map(int, input().split()))

    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + v[i]

    ans = -inf
    for i in range(n):
        for j in range(i, n):
            sum1 = pre[j + 1] - pre[i]
            for k in range(j + 1, n):
                for l in range(k, n):
                    sum2 = pre[l + 1] - pre[k]
                    ans = max(ans, sum1 + sum2)

    print(str(ans) + "\n")


if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        solve()

    input_file.close()
    output_file.close()
