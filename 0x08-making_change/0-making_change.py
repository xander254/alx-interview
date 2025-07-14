#!/usr/bin/python3
"""
Making Change module
"""


def makeChange(coins, total):
    """Determine fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    # Optimization: Sort coins once
    coins.sort()

    # DP array: dp[x] = minimum coins to make x
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins to make amount 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != float('inf') else -1
