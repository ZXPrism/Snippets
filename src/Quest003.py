# created: 15:24 2024/10/11 by ZXPrism
# https://tieba.baidu.com/p/9214597436

# Powered by ChatGPT 4o


def min_ones_dp_with_composition(target):
    # Initialize dp array where dp[n] represents the minimum number of 1s needed for number n
    dp = [float("inf")] * (target + 1)

    # Initialize composition array to store the best expression for each n
    composition = [""] * (target + 1)

    # Base case: dp[1] = 1 and the composition is just "1"
    dp[1] = 1
    composition[1] = "1"

    # Fill the dp and composition array for each number from 2 to target
    for n in range(2, target + 1):
        # Try addition: dp[n] = dp[i] + dp[n - i] for all i < n
        for i in range(1, n):
            if dp[n] > dp[i] + dp[n - i]:
                dp[n] = dp[i] + dp[n - i]
                composition[n] = f"({composition[i]} + {composition[n - i]})"

        # Try multiplication: dp[n] = dp[i] + dp[n // i] for all i where n % i == 0 and i > 1
        for i in range(2, n):
            if n % i == 0 and dp[n] > dp[i] + dp[n // i]:
                dp[n] = dp[i] + dp[n // i]
                composition[n] = f"({composition[i]} * {composition[n // i]})"

    return dp[target], composition[target]


# Example usage
# for i in range(1, 100):
#     target_number = i
#     min_ones, expression = min_ones_dp_with_composition(target_number)
#     print(f"{i} uses {min_ones} ones: {expression}")

print(min_ones_dp_with_composition(23 * 25))
