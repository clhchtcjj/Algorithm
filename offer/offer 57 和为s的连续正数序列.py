# -*- coding:utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
    def getSequence(self,s,nums):
        if len(nums) <1 or s < 0:
            return 0
        i = 0
        j = 1
        curr_sum = nums[i]
        lens = None
        while j <= len(nums) and i <= j-1:
            print(curr_sum,lens,i,j-1)
            if curr_sum >= s:
                ans = nums[i:j]
                if lens is None or lens > len(ans):
                    lens = len(ans)
                i += 1
                if i >= j and j < len(nums):
                    j += 1
                    curr_sum += nums[j-1]
                curr_sum -= (nums[i-1])
            else:
                j += 1
                if j-1 > len(nums)-1:
                    break
                curr_sum += nums[j-1]
        if lens == None:
            return 0
        return lens


if __name__ == "__main__":
    S = Solution()
    print(S.getSequence(3,[1,1]))

