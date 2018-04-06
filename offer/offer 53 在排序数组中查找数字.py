# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 在排序数组中统计某一数字出现次数
# 排序=》二分
# 查找第一个出现的位置和最后一个出现的位置

class Solution():
    def GetNumberOfK(self, data, k):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(data) == 0:
            return 0
        left_id = self.searchFirst(data,k,0,len(data)-1)
        right_id = self.searchLast(data,k,0,len(data)-1)
        if left_id != -1 and right_id != -1:
            return right_id-left_id+1
        else:
            return 0

    def searchFirst(self,nums,target,s,t):
        if s <= t:
            mid = (s+t) // 2
            if nums[mid] == target:
                if mid-1 >= s and nums[mid-1] == target:
                    return self.searchFirst(nums,target,s,mid-1)
                # elif mid+1 <= t and nums[mid+1] == target:
                #     return self.searchFirst(nums,target,mid+1,t)
                elif s <= mid <= t:
                    return mid
            elif nums[mid] < target:
                return self.searchFirst(nums,target,mid+1,t)
            else:
                return self.searchFirst(nums,target,s,mid-1)
        return -1

    def searchLast(self,nums,target,s,t):
        if s <= t:
            mid = (s+t)//2
            if nums[mid] == target:
                if mid+1 <= t and nums[mid+1] == target:
                    return self.searchLast(nums,target,mid+1,t)
                elif s <= mid <= t:
                    return mid
            elif nums[mid] < target:
                return self.searchLast(nums,target,mid+1,t)
            else:
                return self.searchLast(nums,target,s,mid-1)
        return -1

if __name__ == "__main__":
    S = Solution()
    print(S.GetNumberOfK([0, 1, 1, 4, 7, 7, 7],4))