# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 数组中k个最小数

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k >= len(tinput):
            return sorted(tinput)
        elif k == 0:
            return []
        else:
            index = self.partition(tinput,0,len(tinput)-1)
            while index != k-1:
                if index < k-1:
                    index = self.partition(tinput,index+1,len(tinput)-1)
                else:
                    index = self.partition(tinput,0,index-1)
        return sorted(tinput[0:k])


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


if __name__ == "__main__":
    S = Solution()
    print(S.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))