# created: 17:20 2024/8/19 by ZXPrism
# version 01
# only applicable to complete binary trees


def LCA(x, y):
    if x == y:
        return x
    return LCA(x >> 1, y) if x > y else LCA(x, y >> 1)


print(LCA(17, 19))  # answer = 4
