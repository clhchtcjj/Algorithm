# -*- encoding: utf-8 -*-
__author__ = 'CLH'

# 队列中的最大值
# 定义一个保存候选最大值的队列
#   1. 看看滑动窗口滑出的是不是队头元素，如果是，则队头元素出队
#   2. 入队的比队尾巴元素大，则依次比较，去掉比自己小的队头
#   3. 入队的比队尾巴元素小，入队

import Queue

class Solution(object):
    def findQueueMax(self,nums,k):
        if len(nums) < k or len(nums) == 0 or k<0:
            return []
        ans = []
        max_candidate = Queue.deque()
        i = 0
        max_candidate.append(i)
        j = i + 1
        while i <= len(nums) - k:
            while j -i <= k-1:
                while len(max_candidate)>0 and nums[max_candidate[-1]] < nums[j]:
                    max_candidate.pop()
                max_candidate.append(j)
                j+=1
            while max_candidate[0] < i:
                max_candidate.popleft()
            ans.append(nums[max_candidate[0]])
            i+=1
        return ans

if __name__ == "__main__":
    S = Solution()
    print(S.findQueueMax([1,3,1,2,0,5],3))