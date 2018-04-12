import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self,root):
        d = collections.Counter()

        def dfs(node):

            if not node:
                return
            # if node.val not in d:
            #     d[node.val] = 1
            # else:
            d[node.val]=d[node.val]+1
            dfs(node.left)
            dfs(node.right)

        if not root:
            return 0
        dfs(root)

        x = max(d.values())
        # max(d, key=d.get)  #获取值最大的键值
        l = list(filter(lambda s:d[s] == x ,d ))
        return l

root = TreeNode(21474836471)



s = Solution()
print(s.helper(root))
dict = {1:2,3:1,4:8}
print(max(dict,key=dict.get))
