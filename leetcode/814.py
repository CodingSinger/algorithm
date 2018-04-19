class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归到最底(没有子节点)，如果最底层是0，则删除，然后往上移，如果该节点也是0，并且子节点都被移除了，则也移除，继续往上移动。依次递归
class Solution:
    def helper(self, root):

        def dfs(node, parent, left):

            if not node:
                return
            dfs(node.left, node, True)
            dfs(node.right, node, False)
            if node.val == 0 and not node.left and not node.right:
                if left:
                    parent.left = None
                else:
                    parent.right = None

        dfs(root.left,root,True)
        dfs(root.right,root,False)
        return root

    def print(self, root):
        if not root:
            return
        self.print(root.left)
        print(root.val)
        self.print(root.right)



root = TreeNode(1)

root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
s = Solution()
root = s.helper(root)
s.print(root)

