# -- coding: utf-8 --
__author__ = 'CLH'

# 旋转数组中查找元素
# 二分，不断分解成子问题，直至子问题变成顺序查找

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low <= high:
                mid = (low + high) / 2
                if nums[mid] == target:
                    return mid
                if nums[low] <= nums[high]:
                    if nums[mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if nums[low] <= nums[mid-1]:
                        if nums[low] <= target and nums[mid-1] >= target:
                            high = mid - 1
                        else:
                            low = mid+1
                    else:
                        if nums[mid+1] <= target and nums[high] >= target:
                            low = mid+1
                        else:
                            high = mid-1

        return -1

if __name__ == "__main__":
    S = Solution()
    print(S.search([4,5,6,7,0,1,2],0))