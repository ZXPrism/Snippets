# created: 22:36 2025/01/23 by ZXPrism
# version 01
# Description: view a PBM file
# the online PBM viewers all suck! I'd rather write one by myself.

# test image: moon.pbm

import sys, re
import numpy as np
import matplotlib.pyplot as plt

argc = len(sys.argv)
if argc != 2:
    print("[PBMViewer] Unknown command!")
    sys.exit(0)

filename = sys.argv[1]
fp = open(filename, encoding="UTF-16")

header = fp.readline().strip()
if header != "P1":
    print(f"[PBMViewer] Unsupported file format! Header: {header}")
    sys.exit(0)

width, height = map(int, fp.readline().split())
if width <= 0 or height <= 0:
    print(f"[PBMViewer] Invalid width {width} or height {height}!")
    sys.exit(0)

img = np.ones((height, width, 3))

data = fp.readlines()
fp.close()

ptr = 0
pattern = "[01]"
for line in data:
    bits = re.findall(pattern, line)
    for bit in bits:
        val = int(bit)
        img[ptr // width][ptr % width] = [val] * 3
        ptr += 1

plt.imshow(img)
plt.show()
