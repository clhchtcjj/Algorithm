# -- coding:utf-8 --
__author__ = 'CLH'


class Solution():
    def __init__(self):
        self.ans = "0"

    def printOneToN(self,n):
        k = n - 1
        max_str = "9"*n
        self.ans = "0"*n
        while 1:
            self.addOneByString(k)
            self.printAns()
            if self.ans == max_str:
                break

    def addOneByString(self,k):
        # 最高位补位
        if k <= 0:
            if int(self.ans[k]) + 1 >= 10:
                self.ans = "1"+str(int(self.ans[k])-9)+self.ans[k+1:]
                return
            else:
                self.ans = str(int(self.ans[k])+1)+self.ans[k+1:]
                return
        if int(self.ans[k]) + 1 >= 10:
            self.ans = self.ans[:k] + str(int(self.ans[k])-9)+self.ans[k+1:]
            return self.addOneByString(k-1)
        else:
            self.ans = self.ans[:k]+str(int(self.ans[k])+1)+self.ans[k+1:]
            return self.ans

    def printAns(self):
        # 去除最高位的0
        i = 0
        for i in range(0,len(self.ans)):
            if self.ans[i] != '0':
                break
        ans = self.ans[i:]
        print(ans)

if __name__ == "__main__":
    S = Solution()
    S.printOneToN(3)
