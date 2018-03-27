# -- coding:utf-8 --
__author__ = 'CLH'

# 判断一个字符串是否为合法数值 A[.[B]][e|EC] .B[e|EC]
# AC为带符号的整数,B为不带符号的整数

class Solution():
    # def __init__(self):

    def isNumber(self,string):
        # 截取A
        A = ""
        start = 0
        nextPart = ""
        for i in range(len(string)):
            if string[i] not in ['.','e','E']:
                A += string[i]
            else:
                start = i
                break
        if string[start] in ['.']:
            nextPart = "point"
        else:
            nextPart = "exponent"

        #截取B
        B = ""
        flagA = self.isSignedInteger(A)
        if flagA and nextPart == "point":
            # B 部分
            for i in range(start+1,len(string)):
                if string[i] not in ['e','E']:
                     B += string[i]
                else:
                    start = i
                    break
            if string[start] in ['e','E']:
                nextPart = "exponent"

        #截取C
        flagB = self.isUnsignedInteger(B,A)
        if flagA and flagB and nextPart == "exponent":
            if len(string[start+1:])> 0 and self.isSignedInteger(string[start+1:]):
                return True
            else:
                return False
        else:
            return flagA & flagB

    def isUnsignedInteger(self,string,A):
        # A为空时，B不能为空
        if string == "" and A!="":
            return True
        elif A == "":
            return False
        for i in range(len(string)):
            if '0' <= string[i] <= '9':
                continue
            else:
                return False
        return True

    def isSignedInteger(self,string):
        if string == "":
            return True
        start = 0
        if string[0] in ['+','-']:
            start += 1
        for i in range(start,len(string)):
            if '0' <= string[i] <= '9':
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    S = Solution()
    print(S.isNumber("."))