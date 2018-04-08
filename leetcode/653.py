

# 该题最先想到的方法就是把每个节点的值都放到字典中，然后判断k-node.val是否在字典中，如果在就返回True
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def helper(self,root,k):

        m = {}
        self.res = False
        def dfs(node):
            if not node:
                return
            m[node.val] = 1
            if k-node.val!= node.val and k-node.val in m :
                self.res = True
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.right= TreeNode(4)
root.left.left = TreeNode(2)
root.right.right = TreeNode(7)
s = Solution()
print(s.helper(root,9))






