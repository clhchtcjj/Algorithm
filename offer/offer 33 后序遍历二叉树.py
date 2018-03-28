# -*- coding:utf-8 -*-
__author__ = 'CLH'

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        else:
            return self.isVerifySquenceOfBST(sequence)

    def isVerifySquenceOfBST(self,sequence):
        if len(sequence) == 1:
            return True
        elif len(sequence) == 0:
            return True
        else:
            root = sequence[-1]
            left = []
            right = []
            for i in range(len(sequence)-2,-1,-1):
                if sequence[i] > root and len(left) == 0:
                    right.append(sequence[i])
                elif sequence[i] < root:
                    left.append(sequence[i])
                else:
                    return False
            left.reverse()
            right.reverse()
            return self.isVerifySquenceOfBST(left) and self.isVerifySquenceOfBST(right)

if __name__ == "__main__":
    S = Solution()
    print(S.VerifySquenceOfBST([]))