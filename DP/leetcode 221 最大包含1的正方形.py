# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 思路：dp[i][j] 表示以i,j 结尾的最大包含1的正方形
import math
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        dp = [[0 for _ in range(m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    if ans < dp[i][j]:
                        ans = dp[i][j]

        for i in range(1,n):
            # print dp
            for j in range(1,m):
                if matrix[i][j] == "1" and matrix[i-1][j-1] == "1":
                    lens = int(math.sqrt(dp[i-1][j-1]))
                    # print lens
                    for k in range(1,lens+1):
                        if matrix[i][j-k] == "1" and matrix[i-k][j] == "1":
                            dp[i][j] = k**2 + 2 * k + 1
                            if ans < dp[i][j]:
                                ans = dp[i][j]
                        else:
                            break
        return ans
