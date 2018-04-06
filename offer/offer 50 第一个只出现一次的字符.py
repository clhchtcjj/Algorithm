# -*- coding:utf-8 -*-
__author__ = 'CLH'

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        seq = []
        count = {}
        for id, char in enumerate(s):
            if count.get(char) is None:
                seq.append([char,id])
                count[char] = 0
            count[char] += 1
        for char,id in seq:
            if count[char] == 1:
                return id
        return -1

if __name__ == "__main__":
    S = Solution()
    print(S.FirstNotRepeatingChar(""))
