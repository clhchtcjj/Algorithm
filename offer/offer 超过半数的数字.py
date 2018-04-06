# -*- coding -*-
__author__ = 'CLH'

import math
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        n = len(numbers)
        if n == 0:
            return 0
        if n == 1:
            return numbers[0]
        index = self.partition(numbers,0,len(numbers)-1)
        while index != math.ceil(n / 2.0):
            if index < math.ceil(n / 2.0):
                index = self.partition(numbers,index+1,len(numbers)-1)
            else:
                index = self.partition(numbers,0,index-1)
        if self.check(numbers[index],numbers):
            return numbers[index]
        else:
            return 0

    def partition(self,nums,s,t):
        pivot = nums[s]
        while s < t:
            while s < t and pivot <= nums[t]:
                t -= 1
            nums[s] = nums[t]
            while s < t and pivot >= nums[s]:
                s += 1
            nums[t] = nums[s]
        nums[s] = pivot
        return s

    def check(self,num,nums):
        cnt = 0
        for i in nums:
            if i == num:
                cnt+=1
        print(len(nums),(len(nums))/2.0,math.ceil((len(nums))/2.0))
        if cnt > math.ceil((len(nums))/2):
            return True
        else:
            return False

    def countFind(self,nums):
        curr = nums[0]
        cnt = 1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        for i in range(1,len(nums)):
            if curr == nums[i]:
                cnt += 1
            else:
                if cnt == 1:
                    curr = nums[i]
                else:
                    cnt -= 1
        if cnt > 0 and self.check(curr,nums):
            return curr
        else:
            return 0

if __name__ == "__main__":

    S = Solution()
    print(S.countFind([4,2,1,4,2,4]))