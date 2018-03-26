__author__ = 'CLH'

import math
class Solution():
    def __init__(self,n,nums):
        self.n = n
        self.nums = nums
        self.ans = 0

    def fenpingguo(self):
        total_sum = sum(self.nums)
        if total_sum % self.n != 0:
            return -1
        avg = int(sum(self.nums)/self.n)
        new_nums = [item - avg for item in self.nums]
        positive_sum = 0
        for num in new_nums:
            if abs(num) % 2 != 0:
                return -1
            elif num > 0:
                positive_sum += num
        return int(positive_sum / 2)


if __name__ == "__main__":
    n = int(input())
    nums = [int(item) for item in input().strip().split(" ")]
    S = Solution(n,nums)
    print(S.fenpingguo())

