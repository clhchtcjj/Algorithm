# -*- coding: utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        dp = [triangle[0][0]]
        for i in range(1,m):
            temp_dp = []
            # print "dp:",dp
            n = len(triangle[i-1])
            for j in range(len(triangle[i])):
                # print dp[max(0,j-1):min(n,j+1)]
                temp_dp.append(triangle[i][j]+min(dp[max(0,j-1):min(n,j+1)]))
            dp = temp_dp
        return min(dp)
