# -*- coding:utf-8 -*-
__author__ = 'CLH'

class Solution:
    def InversePairs(self, data):
        # write code here
        if len(data) == 0:
            return 0
        else:
            copy = list(data)
            count = self.InversePairsCore(data,copy,0,len(data)-1)
            # print(copy,data)
            return count

    def InversePairsCore(self,data,copy,s,t):
        # print(s,t)
        if s == t:
            copy[s] = data[s]
            return 0
        length = (t-s) // 2
        # map阶段
        left = self.InversePairsCore(copy,data,s,s+length)
        right = self.InversePairsCore(copy,data,s+length+1,t)
        # reduce阶段
        num_left_end = s+length
        num_right_end = t
        copy_index = t
        count = 0
        while num_left_end >= s and num_right_end >= s+length+1:
            if data[num_left_end] >= data[num_right_end]:
                    count += num_right_end - s-length
                    copy[copy_index] = data[num_left_end]
                    copy_index -= 1
                    num_left_end -= 1
            else:
                copy[copy_index] = data[num_right_end]
                copy_index -= 1
                num_right_end -= 1
        while num_left_end >= s:
            copy[copy_index] = data[num_left_end]
            copy_index -= 1
            num_left_end -= 1
        while num_right_end >= s+length+1:
            copy[copy_index] = data[num_right_end]
            copy_index -= 1
            num_right_end -= 1
        return left + right + count


if __name__ == "__main__":
    S = Solution()
    print(S.InversePairs([1,2,3,4,5,6,7,0]))
# [233,2000000001,234,2000000006,235,2000000003,236,2000000007,237,2000000002,2000000005,233,233,233,233,233,2000000004]