__author__ = 'CLH'

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# 给定两个有序数组，合并成一个有序数组
# 思路：从后往前

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 or len(nums1) == 0:
            nums1[:] = nums2[:]
        elif n == 0 or len(nums2) == 0:
            nums1[:] = nums1[:]
        else:
            # nums1.extend([0]*n)
            ptr_A = m-1
            ptr_B = n-1
            for i in range(len(nums1)-1,-1,-1):
                if ptr_A < 0:
                    nums1[i] = nums2[ptr_B]
                    ptr_B -= 1
                    continue
                if ptr_B < 0:
                    nums1[i] = nums1[ptr_A]
                    ptr_A -= 1
                    continue
                if nums1[ptr_A] >= nums2[ptr_B]:
                    nums1[i] = nums1[ptr_A]
                    ptr_A -= 1
                else:
                    nums1[i] = nums2[ptr_B]
                    ptr_B -= 1
        print(nums1)

    # # 简单解法
    # def merge(self, nums1, m, nums2, n):
    #     while m > 0 and n > 0:
    #         if nums1[m-1] >= nums2[n-1]:
    #             nums1[m+n-1] = nums1[m-1]
    #             m -= 1
    #         else:
    #             nums1[m+n-1] = nums2[n-1]
    #             n -= 1
    #     if n > 0:
    #         nums1[:n] = nums2[:n]

if __name__ == "__main__":
    S = Solution()
    S.merge([1,0],1,[2],1)
    # print(S.nums)