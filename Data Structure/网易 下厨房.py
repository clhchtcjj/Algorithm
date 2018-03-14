__author__ = 'CLH'

'''
    这题说白了就是统计不同单词数
    用前缀树加快搜索
    注意点：python如何读取多行输入
'''
import sys
class TrieNode():
    def __init__(self):
        self.childs = {}
        self.word = False

class Solution():
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def add(self,word):
        node = self.root
        for char in word:
            if node.childs.get(char) is None:
                node.childs[char] = TrieNode()
            node = node.childs[char]
        if node.word == False:
            node.word = True
            self.size += 1

if __name__ == "__main__":
    words = []
    for line in sys.stdin:
        words.extend(line.strip().split(" "))
    S = Solution()
    for word in words:
        S.add(word)
    print(S.size)
