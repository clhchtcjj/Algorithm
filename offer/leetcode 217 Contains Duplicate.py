__author__ = 'CLH'

class Solution():
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        has_num ={}
        for num in nums:
            if num in has_num:
                return True
            has_num[num] = 1
        return False

if __name__ == "__main__":
    S = Solution()
    print(S.containsDuplicate([1,2,2]))