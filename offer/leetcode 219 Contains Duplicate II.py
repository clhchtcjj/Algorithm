__author__ = 'CLH'


class Solution():
    # 暴力解法，无法AC
    # # def containsNearbyDuplicate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     for i in range(len(nums)):
    #         if i == len(nums)-1:
    #             return False
    #         for j in range(i+1,min(i+k+1,len(nums))):
    #             if nums[i] == nums[j]:
    #                 return True
    #     return False

    # # 简单解法，一次遍历，维护一个字典记录最新下标(HashMap)
    # def containsNearbyDuplicate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     num_index = {}
    #     for i in range(len(nums)):
    #         if num_index.get(nums[i]) is None:
    #             num_index[nums[i]] = i
    #         elif i - num_index[nums[i]]> k:
    #             num_index[nums[i]] = i
    #         else:
    #             return True
    #     return False

    # 简单解法，一次遍历，维护一个字典记录最新下标(HashSet)
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        for i in range(0,min(k+1,len(nums))):
            if nums[i] in window:
                return True
            else:
                window.add(nums[i])
        for i in range(k+1,len(nums)):
            window.remove(nums[i-k-1])
            if nums[i] in window:
                return True
            else:
                window.add(nums[i])
        return False


if __name__ == "__main__":
    S = Solution()
    print(S.containsNearbyDuplicate([1,2,1,1],0))