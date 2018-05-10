# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 思路：dp[i] 以nums[i]结尾的最大子串和

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [nums[0]]
        for i in range(1,len(nums)):
            dp.append(max(nums[i],nums[i]+dp[-1]))
        return max(dp)