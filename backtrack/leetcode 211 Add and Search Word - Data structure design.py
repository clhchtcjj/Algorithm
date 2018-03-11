__author__ = 'CLH'

'''
    构造字典树
'''

class TrieNode(object):
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word):
        return self.searchFrom(self.root, word)

    def searchFrom(self, node, word):
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for k in node.children:
                    if self.searchFrom(node.children[k], word[i+1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            node = node.children[c]
        return node.word

if __name__ == "__main__":

    obj = WordDictionary()
    # obj.addWord("a")
    # obj.addWord("ab")
    # # obj.addWord("a")
    # # obj.addWord("runs")
    # # obj.addWord("add")
    # # obj.addWord("adds")
    # # obj.addWord("adder")
    # # obj.addWord("addee")
    # # param_1 = obj.search("a.")
    # param_1 = obj.search("a.")
    # param_2 = obj.search("ab")
    # param_3 = obj.search(".a")
    # param_4 = obj.search(".b")
    # param_5 = obj.search("ab.")
    # param_6 = obj.search(".")
    # param_7 = obj.search("..")
    # param_8 = obj.search("..")
    # print(param_1,param_2,param_3,param_4,param_5,param_6,param_7,param_8)

    obj.addWord("ran")
    obj.addWord("rune")
    obj.addWord("runner")
    obj.addWord("runs")
    obj.addWord("add")
    obj.addWord("adds")
    obj.addWord("adder")
    obj.addWord("addee")
    param_1 = obj.search("r.n")
    param_2 = obj.search("ru.n.e")
    param_3 = obj.search("add")
    param_4 = obj.search("add.")
    param_5 = obj.search("adde.")
    param_6 = obj.search("ab.")
    param_7 = obj.search("...")
    param_8 = obj.search("..")
    print(param_1,param_2,param_3,param_4,param_5,param_6,param_7,param_8)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)