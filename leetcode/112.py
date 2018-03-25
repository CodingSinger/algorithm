class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root, sum):

        def dfs(root, nows):

            if not root:
                return

            if not root.left and not root.right and nows + root.val == sum:

                self.flag = True
            else:

                dfs(root.left, nows + root.val)
                dfs(root.right, nows + root.val)

        self.flag = False

        dfs(root, 0)
        return self.flag


s = Solution()
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(-2)
root.left.left.left = TreeNode(-1)

root1 = TreeNode(-2)
root1.right = TreeNode(-3)
print(s.helper(root, -1))
