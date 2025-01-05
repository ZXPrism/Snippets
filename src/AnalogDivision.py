# created: 09:33 2024/10/18 by ZXPrism

x = 114514  # dividend, 32-bit unsigned -> implicitly extended to 64-bit
y = 1919  # divisor, 32-bit unsigned

if x < 0 or x >= (1 << 32) or y <= 0 or y >= (1 << 32):
    print(f"Invalid arguments {x} {y}!")
    exit()

result = x

for i in range(33):  # careful, quotient would have 33 bits!
    h32 = result >> 32
    if h32 >= y:
        result -= y << 32
        result <<= 1
        result |= 1
    else:
        result <<= 1

print(f"[Actual Result] Q: {x // y}, R: {x % y}")
print(
    f"[Analog Result] Q: {result % (1 << 31)}, R: {result >> 33}"
)  # the last left shift is meaningless, so we shift for extra 1 bit
