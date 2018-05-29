# -*- coding:utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total_sum = sum(nums)
        target = (S + total_sum) // 2
        if (S + total_sum) % 2 == 1:
            return 0
        if total_sum < S:
            return 0
        n = len(nums)
        if n == 0 and S == 0:
            return 1
        if n == 0 and S != 0:
            return 0
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] += dp[i-num]
        return dp[target]


if __name__ == "__main__":
    S = Solution()
    print(S.findTargetSumWays([7,9,3,8,0,2,4,8,3,9],0))