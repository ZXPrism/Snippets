from random import randint

N = int(1e4)

x = randint(0, N)
n = randint(0, N)
m = randint(0, N)
k = randint(1, n + m)

a = [randint(0, N) for _ in range(n)]
b = [randint(1, N) for _ in range(m)]

print(x, n, m, k)
print(" ".join(map(str, a)))
print(" ".join(map(str, b)))
