# -- coding: utf-8 --
__author__ = 'CLH'

# 旋转数组中找最小值
# 思路：二分查找：如何中间值大于右指针，则最小数在右边（low = mid），否则在左边或就是自己（high=mid）。最终low到达最小数的前一个位置
#       当数组中出现重复数字时，只能顺序遍历；当数组就是有序的，则直接返回

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        mid = 0
        while nums[low] >= nums[high]:
            if high-low == 1:
                mid = high
                break
            else:
                mid = int((low+high) / 2)
                if nums[mid] == nums[low] and nums[mid] == nums[high]:
                    return self.MinInorder(nums)
                if nums[mid] > nums[high]:
                    low = mid
                else:
                    high = mid

        return nums[mid]


    def MinInorder(self,nums):
        ans = nums[0]
        for i in nums:
            if ans > i:
                ans = i
        return ans



if __name__ == "__main__":
    S = Solution()
    print(S.findMin([1,1,1]))