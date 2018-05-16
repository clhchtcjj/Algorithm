# -*- coding: utf-8 -*-
__author__ = 'CLH'



class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n<1:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        dp = [nums[0],nums[1]]
        for i in range(2, n):
            dp.append(max(dp[0:i-1])+nums[i])
        return max(dp)