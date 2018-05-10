# -*- coding: utf-8 -*-
__author__ = 'CLH'

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # dp = [[0 for _ in range(n)] for _ in range(m)]
        # for i in range(m):
        #     dp[i][0] = 1
        # for j in range(n):
        #     dp[0][j] = 1
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # return dp[m-1][n-1]
        # 压缩dp空间
        dp = [1 for _ in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j - 1]
        return dp[-1]