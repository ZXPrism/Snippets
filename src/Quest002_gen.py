# created: 22:43 2024/10/10 by ZXPrism
# https://tieba.baidu.com/p/9213589527

import random

t = 100

input_data = open("input.txt", "w")
input_data.write(str(t) + "\n")

for i in range(t):
    n = random.randint(2, 100)
    v = [str(random.randint(-2000, 2000)) for _ in range(n)]
    input_data.write(str(n) + "\n")
    input_data.write(" ".join(v) + "\n")

input_data.close()
