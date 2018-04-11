# -*- coding:utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        sums = [0] * (amount+1)
        for i in range(1,amount+1):
            min_num = None
            for coin in coins:
                if i - coin >= 0:
                    if sums[i-coin] is not None:
                        if min_num is None or min_num > sums[i-coin]:
                            min_num = sums[i-coin]
            if min_num is not None:
                sums[i] = min_num + 1
            else:
                sums[i] = None
        if sums[amount] is not None:
            return sums[amount]
        else:
            return -1

    def coinChange2(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        for j in range(0,len(coins)):
            for i in range(amount+1):
                if i-coins[j] >= 0:
                    dp[i] += dp[i-coins[j]]
        return dp[-1]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 5
    S = Solution()
    print(S.coinChange2(amount,coins))