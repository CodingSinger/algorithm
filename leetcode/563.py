import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def helper(self,root):

        self.res = 0
        def dfs(node, mathleft=None):
            if not node:
                return 0
            else:
                left = dfs(node.left) #获取左子树上的所有节点值
                right = dfs(node.right) # 获取右子树上所有节点值
                self.res += abs(left-right)

                return left+right+node.val #记住该是获取子树所有节点值的方法
        dfs(root)
        return self.res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
s = Solution()

print(s.helper(root))







