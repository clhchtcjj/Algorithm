# -*- coding: utf-8 -*-
__author__ = 'CLH'

# dp[n] = dp[n]+dp[n-nums[i]]

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        n = len(nums)
        for i in range(target+1):
            for j in range(0, n):
                if i >= nums[j]:
                    dp[i] = dp[i] + dp[i-nums[j]]
            print(dp)
        return dp[target]



if __name__ == "__main__":
    S = Solution()
    print(S.combinationSum4([1,2,3],4))