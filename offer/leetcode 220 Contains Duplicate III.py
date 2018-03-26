__author__ = 'CLH'

'''
    问题：给定一个整数数组，判断其中是否存在两个不同的下标i和j满足：| nums[i] - nums[j] | <= t 并且 | i - j | <= k
    如果： floor(nums[j] / t) ∉ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 非d
    推出： | nums[i] - nums[j] | > t   非a
    遍历数组nums时，检查nums[i]与键集{floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}对应的值的差值即可。
'''

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: return False
        dic,w = dict(),t+1
        for i in range(len(nums)):
            m = nums[i]/w
            if m in dic: return True
            if m-1 in dic and abs(nums[i]-dic[m-1]) < w: return True
            if m+1 in dic and abs(nums[i]-dic[m+1]) < w: return True
            dic[m] = nums[i]
            if i >= k: del dic[nums[i-k]/w]
        return False


if __name__ == "__main__":
    S = Solution()
    print(S.containsNearbyAlmostDuplicate([-1,-1],1,0))
