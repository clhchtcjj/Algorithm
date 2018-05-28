# encoding: utf-8 -*-
__author__ = 'CLH'

# 思路： dp[i] = min(dp[i-1],dp[i-2])+cost[i]
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n == 1:
            return cost[0]
        dp = [cost[0],cost[1]]
        for i in range(2,n):
            dp.append(min(dp[i-1],dp[i-2])+cost[i])

        return min(dp[-1],dp[-2]) # 注意返回值
