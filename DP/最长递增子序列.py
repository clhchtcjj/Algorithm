# -*- coding:utf-8 -*-
__author__ = 'CLH'

class Solution():
    def LIS1(self,nums):
        '''
        nlogn
        :param nums:
        :return:
        '''
        B = [0]
        n = len(nums)
        if n == 0:
            return len(B)-1
        B.append(nums[0])
        for i in range(1,n):
            # 二分查找插入位置
            pos = self.binarySearch(B,nums[i],0,len(B)-1)
            if pos == len(B):
                B.append(nums[i])
            else:
                B[pos] = nums[i]
        return len(B)-1

    def binarySearch(self,nums,k,s,t):
        if  s <= t:
            mid = (s+t) // 2
            if k == nums[mid]:
                return mid
            if k < nums[mid]:
                return self.binarySearch(nums,k,s,mid-1)
            else:
                return self.binarySearch(nums,k,mid+1,t)
        return s


if __name__ == "__main__":
    S = Solution()
    print(S.LIS1([]))