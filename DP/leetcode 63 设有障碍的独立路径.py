# -*- coding: utf-8 -*-
__author__ = 'CLH'

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = []
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                dp += [0] * (n-i)
                break
            else:
                dp.append(1)

        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                dp[0]=0
            for j in range(1,n):
                print dp
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]
        return dp[-1]