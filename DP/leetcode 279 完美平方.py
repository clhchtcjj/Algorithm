# -*- coding: utf-8 -*-
__author__ = 'CLH'

"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""

"""
dp[i]: i 的perfect square
dp[i] = min(dp[i-j*j]+1) j>=1 and j*j <= i.
dp[0] = 1

"""
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [1,1]
        square = [1]
        for i in range(2,n+1):
            s = int(math.sqrt(i))
            if s ** 2 > square[-1]:
                square.append(s ** 2)
                dp.append(1)
            else:
                min_num = float('inf')
                for s in square:
                    if min_num > dp[i-s]:
                        min_num = dp[i-s]
                dp.append(min_num + 1)
            # print dp
        return dp[n]
