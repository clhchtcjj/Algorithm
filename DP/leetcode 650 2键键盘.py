# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 思路 dp[i]=min(dp[i],dp[j]+i/j),i>1,j<i且i是j的整数倍


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 0:
            return 0
        dp = [1001 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            for j in range(1,i):
                if i % j == 0:
                    dp[i] = min(dp[i],dp[j]+i//j)
        return dp[n]
if __name__ == "__main__":
    S = Solution()
    print(S.minSteps(25))
