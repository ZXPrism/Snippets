# created: 09:33 2024/10/18 by ZXPrism

x = 12345  # multiplier 1, 32-bit unsigned
y = 56789  # multiplier 2, 32-bit unsigned

if x < 0 or x >= (1 << 32) or y < 0 or y >= (1 << 32):
    print(f"Invalid arguments {x} {y}!")
    exit()

result = y

# these procedures can be easily realized by hardware, no "multiplications"!
# but requires a shift register, thus using multiple clocks
for i in range(32):
    h32 = result >> 32
    if result & 1:
        h32 += x
    result >>= 1
    result = (result & ((1 << 31) - 1)) + (h32 << 31)

print(f"Actual Value: {x * y}")
print(f"Analog Multiplication Result: {result % (1 << 32)}")
