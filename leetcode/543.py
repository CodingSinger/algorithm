
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def helper(self,root):

        self.res = 0
        def dfs(node):

            if not node:
                return 0
            ldepth = dfs(node.left)+1
            rdepth = dfs(node.right)+1  # 每往下一层加1
            return max(ldepth,rdepth) # 取出左子树和右子树中最大的就是这棵树的最大高度

        def allNode(root):  # 遍历每个节点 分别计算每个节点的左子树和右子树的高度，高度相加就是该节点为根的树的最大直径


            if not root:
                return
            self.res = max(dfs(root.left)+dfs(root.right),self.res)

            allNode(root.left)
            allNode(root.right)

        allNode(root)

        return self.res
s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(s.helper(root))




