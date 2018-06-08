# -*- coding:utf-8 -*-
__author__ = 'CLH'

class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        sums = [nums[i] for i in range(n)]
        if n == 0:
            return False
        for lens in range(2, n+1):
            for i in range(0, n-lens+1):
                sums[i] += nums[i+lens-1]
                if sums[i] == 0:
                    return True
                elif k!=0 and sums[i] % k == 0:
                    return True
        return False

if __name__ == "__main__":
    S = Solution()
    print(S.checkSubarraySum([0,1,0],0))
